import asyncio
from src.flappy import Flappy

async def handler(request):
    flappy = Flappy()
    await flappy.start()
    return {
        "statusCode": 200,
        "body": "Flappy started successfully"
    }

if __name__ == "__main__":
    asyncio.run(handler(None))  # Test locally if needed
