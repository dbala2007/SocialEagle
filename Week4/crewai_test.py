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
    role="Writer",
    goal="Write short and simple text",
    backstory="You love writing and clearly write for beginners",
    llm=deepseek_llm,
    verbose=True
)

write_poem = Task(
    description="Write a 2 line short poem about the sun",
    expected_output="A simple 2 line poem",
    agent=writer
)

writer_crew = Crew(
    agents=[writer],
    tasks=[write_poem]
)

result = writer_crew.kickoff()

print(result)