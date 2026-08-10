from crewai import Agent, Task, Crew, LLM, Process
from dotenv import load_dotenv
import os

load_dotenv()

deepseek_llm = LLM(
    model="deepseek/deepseek-chat",  # Or "deepseek/deepseek-reasoner" for R1
    api_key=os.environ["DEEPSEEK_API_KEY"],
    temperature=0.5,
)

researcher = Agent(
    role="Researcher",
    goal="Find facts",
    backstory="You find facts",
    llm=deepseek_llm,
    verbose=True
)

writer = Agent(
    role="Writer",
    goal="Write simply",
    backstory="You write for beginners",
    llm=deepseek_llm,
    verbose=True
)

job = Task(
    description="Research and then write 3 lines about ocean",
    expected_output="3 short lines",
)

crew = Crew(agents=[researcher,writer], tasks=[job], process=Process.hierarchical, manager_llm=deepseek_llm)

result = crew.kickoff()

print(result)
