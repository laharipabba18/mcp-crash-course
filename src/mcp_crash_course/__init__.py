import asyncio
from dotenv import load_dotenv
import os
 
from mcp import ClientSession,StdioServerParameters
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.prebuilt import create_react_agent
from mcp.client.stdio import stdio_client


load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

stdio_server_params=StdioServerParameters(
    command="python",
    args=["C:\\Users\\PABBALAHARI\\mcp-crash-course\\servers\\weather_server.py"],
)

async def main() -> None:
    print("Hello from mcp-crash-course!")
    
if __name__ == "__main__":
    asyncio.run(main())
