import sys, os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, LLM
from crewai_tools import MCPServerAdapter
from mcp import StdioServerParameters

load_dotenv()

server_params = StdioServerParameters(command=sys.executable, args=["mcp_math_server.py"])

deepseek_llm = LLM(
    model="deepseek/deepseek-chat",  # Or "deepseek/deepseek-reasoner" for R1
    api_key=os.environ["DEEPSEEK_API_KEY"],
    temperature=0.5,
)

with MCPServerAdapter(server_params) as mcp_tools:
    agent = Agent(
        role="Math Helper",
        goal="Solve math using the MCP tools",
        backstory="You always use the tools from the MCP Server",
        tools=mcp_tools,
        llm=deepseek_llm,
        verbose=True
    )

    task = Task(
        description="What is 8 plus 5? Use the tool to add",
        expected_output="The sum of two numbers",
        agent=agent
    )

    crew = Crew(agents=[agent], tasks=[task])

    result = crew.kickoff()

    print(result)