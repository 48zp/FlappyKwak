import asyncio
from src.flappy import Flappy

# Create a start function that Vercel can directly invoke
async def main():
    flappy = Flappy()
    await flappy.start()
    return "Flappy started successfully"

# Run the async main function if the file is executed as a script
if __name__ == "__main__":
    asyncio.run(main())
