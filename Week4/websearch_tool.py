from dotenv import load_dotenv

load_dotenv()

import os
from crewai import Agent, LLM, Task, Crew
from crewai_tools import SerpApiGoogleSearchTool

serch_tool = SerpApiGoogleSearchTool()

deepseek_llm = LLM(
    model="deepseek/deepseek-chat",  # Or "deepseek/deepseek-reasoner" for R1
    api_key=os.environ["DEEPSEEK_API_KEY"],
    temperature=0.5,
)

researcher = Agent(
    role="Researcher",
    goal="Find current information from web",
    backstory="You search the internet for fresh facts",
    tools=[serch_tool],
    llm=deepseek_llm,
    verbose=True
)

task = Task(
    description="Search the web and tell me once recent news headline about AI",
    expected_output="One recent headline with a short note",
    agent=researcher
)

crew = Crew(agent=[researcher], tasks=[task])

result = crew.kickoff()

print(result)
