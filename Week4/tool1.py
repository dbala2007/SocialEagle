from dotenv import load_dotenv

load_dotenv()

import os
from crewai import Agent, LLM, Task, Crew
from crewai_tools import FileReadTool

deepseek_llm = LLM(
    model="deepseek/deepseek-chat",  # Or "deepseek/deepseek-reasoner" for R1
    api_key=os.environ["DEEPSEEK_API_KEY"],
    temperature=0.5,
)

read_tool = FileReadTool()

reader = Agent(
    role="File Reader",
    goal="Read files and answer about them",
    backstory="You carefully read files",
    tools=[read_tool],
    llm=deepseek_llm,
    verbose=True
)

task = Task(
    description="Read the crewai_test.py file in this folder",
    expected_output="Read the file",
    agent=reader
)

crew = Crew(agent=[reader], tasks=[task])

result = crew.kickoff()

print(result)
