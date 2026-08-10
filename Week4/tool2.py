from dotenv import load_dotenv

load_dotenv()

import os
from crewai import Agent, LLM, Task, Crew
from crewai.tools import tool

@tool("Add Tool")
def add_numbers(a: int, b:int) -> int:
    """Add two numbers and return the result"""
    return a+b

deepseek_llm = LLM(
    model="deepseek/deepseek-chat",  # Or "deepseek/deepseek-reasoner" for R1
    api_key=os.environ["DEEPSEEK_API_KEY"],
    temperature=0.5,
)

math_agent = Agent(
    role="Math Helper",
    goal="Solve simple math using tools",
    backstory="You always use your tools to calculate",
    tools=[add_numbers],
    llm=deepseek_llm,
    verbose=True
)

task = Task(
    description="What is 500 + 25?",
    expected_output="The sum of the numbers provided",
    agent=math_agent
)

crew = Crew(agent=[math_agent], tasks=[task])

result = crew.kickoff()

print(result)
