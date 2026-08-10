from crewai import Agent, Task, Crew, LLM, Process
from dotenv import load_dotenv
import os

load_dotenv()

deepseek_llm = LLM(
    model="deepseek/deepseek-chat",  # Or "deepseek/deepseek-reasoner" for R1
    api_key=os.environ["DEEPSEEK_API_KEY"],
    temperature=0.5,
)

writer = Agent(
    role="Writer",
    goal="Write simply",
    backstory="You write for beginners",
    llm=deepseek_llm,
    verbose=True
)

task = Task(
    description="Write one fun facts about cats",
    expected_output="One fun fact about cats",
    agent=writer
)

crew = Crew(agent=[writer], tasks=[task], process=Process.sequential)

result = crew.kickoff()

print(result)
