"""
AutoGen workflow: read TLDR AI and get the latest GenAI research article.

Uses one AssistantAgent with a tool that fetches and parses TLDR AI;
the agent then selects and summarizes the latest research article on GenAI.

Requires Python 3.10+ (for autogen-ext).
"""
import asyncio
import os
import sys

if sys.version_info < (3, 10):
    print("This workflow requires Python 3.10 or newer (autogen-ext dependency).")
    sys.exit(1)

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient

from tldr_fetcher import get_latest_tldr_ai_research


def get_tldr_ai_latest_research() -> str:
    """
    Fetch the latest TLDR AI newsletter and return research/GenAI articles.
    Use this to find the most recent research article on generative AI.
    """
    return get_latest_tldr_ai_research()


async def run_workflow() -> None:
    """Run the AutoGen workflow: TLDR AI -> latest GenAI research article."""
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("Set OPENAI_API_KEY in your environment (or .env) to run this workflow.")
        return

    model_client = OpenAIChatCompletionClient(
        model="gpt-4o-mini",
        api_key=api_key,
    )

    agent = AssistantAgent(
        name="research_assistant",
        model_client=model_client,
        tools=[get_tldr_ai_latest_research],
        max_tool_iterations=3,
        reflect_on_tool_use=True,
        system_message=(
            "You help users find the latest research on generative AI (GenAI). "
            "When asked for the latest GenAI research article from TLDR AI, use the "
            "get_tldr_ai_latest_research tool to fetch the current TLDR AI content, "
            "then pick the single best/most relevant research article on GenAI (e.g. "
            "LLMs, agents, models, benchmarks) and summarize it clearly: title, source URL, "
            "and a short summary. Reply in a concise, readable way. Say TERMINATE when done."
        ),
    )

    task = (
        "Read TLDR AI and get the latest research article on GenAI. "
        "Use your tool to fetch TLDR AI, then tell me which article is the latest "
        "research-focused one and give me its title, link, and a brief summary."
    )

    print("Running AutoGen workflow: TLDR AI → latest GenAI research\n")
    result = await agent.run(task=task)

    # Print final assistant reply (last message from the agent)
    if result.messages:
        last = result.messages[-1]
        content = getattr(last, "content", None) or ""
        if content:
            print(content.replace("TERMINATE", "").strip())


def main() -> None:
    asyncio.run(run_workflow())


if __name__ == "__main__":
    main()
