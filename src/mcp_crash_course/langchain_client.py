import asyncio

from dotenv import load_dotenv
import os
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.prebuilt import create_react_agent

load_dotenv()

async def main():
    print("Hello langchain MCP")
    
if __name__ == "__main__":
    asyncio.run(main())