from crewai import Agent, Task, Crew, LLM
from dotenv import load_dotenv
import os

print("Crew AI is ready to use")

load_dotenv()

deepseek_llm = LLM(
    model="deepseek/deepseek-chat",  # Or "deepseek/deepseek-reasoner" for R1
    api_key=os.environ["DEEPSEEK_API_KEY"],
    temperature=0.5,
)

writer = Agent(
    role="Content Writer",
    goal="Create Simple Clear Content in Tanglish (Tamil + English)",
    backstory="You write simple contents for Beginners with hook line",
    llm=deepseek_llm,
    verbose=True
)

task1 = Task(
    description="List 3 fun facts about Tamil Nadu",
    expected_output="3 fun facts about Tamil Nadu",
    agent=writer
)

task2 = Task(
    description="Use the facts provided to write one short tweet",
    expected_output="One short tweet with the facts provided",
    agent=writer
)

crew = Crew(agent=[writer], tasks=[task1, task2])

result = crew.kickoff()

print(result)
