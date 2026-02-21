import asyncio
from rescue_agent import RescueAgent

async def main():
    agent = RescueAgent()
    await agent.run()

if __name__ == "__main__":   
    asyncio.run(main())