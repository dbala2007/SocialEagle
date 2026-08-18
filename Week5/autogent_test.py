import asyncio
from dotenv import load_dotenv

from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.agents import AssistantAgent


load_dotenv()


async def main():

    model_client = OpenAIChatCompletionClient(
        model="gpt-4o-mini"
    )

    assistant = AssistantAgent(
        name="assistant",
        model_client=model_client,
        system_message="You are a friendly helper. Keep answers short",
    )

    result = await assistant.run(task="Give me one fun fact about the moon")

    print(result.messages[-1].content)

    # reply = await model_client.create(
    #     [
    #         UserMessage(
    #             content="Say hello in 3 words",
    #             source="user"
    #         )
    #     ]
    # )

    # print("Reply:", reply.content)

    await model_client.close()


asyncio.run(main())