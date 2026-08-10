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

reporter = Agent(
    role="Reporter",
    goal="Find key facts about the topic",
    backstory="You gather clear and true facts",
    llm=deepseek_llm,
    verbose=True
)

editor = Agent(
    role="Editor",
    goal="Turn facts into a short and neat article",
    backstory="You write simple and polished articles",
    llm=deepseek_llm,
    verbose=True
)

find_task = Task(
    description="Find 3 key facts about Electric Vehicle",
    expected_output="3 short facts about Electric Vehicle",
    agent=reporter
)

write_article = Task(
    description="Use the facts to write a 4 sentence article",
    expected_output="A 4 sentence article about the facts provided",
    agent=editor
)

crew = Crew(agent=[reporter, editor], tasks=[find_task, write_article])

result = crew.kickoff()

print(result)
