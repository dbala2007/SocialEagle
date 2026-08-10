from dotenv import load_dotenv

load_dotenv()

import os
from crewai import Agent, LLM, Task, Crew

deepseek_llm = LLM(
    model="deepseek/deepseek-chat",  # Or "deepseek/deepseek-reasoner" for R1
    api_key=os.environ["DEEPSEEK_API_KEY"],
    temperature=0.5,
)

writer = Agent(
    role="Writer",
    goal="Write a short message",
    backstory="You write friendly messages",
    llm=deepseek_llm,
    verbose=True
)

task = Task(
    description="Write a one line thank you message to a customer",
    expected_output="A one line thank you message",
    agent=writer,
    human_input=True
)

crew = Crew(agent=[writer], tasks=[task], memory=True)

result = crew.kickoff()

print(result)
