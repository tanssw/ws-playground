import asyncio
import websockets

from datetime import datetime

async def echo(websocket):
    async for message in websocket:
        # Send every 1 seconds 3 times
        await websocket.send(f'{message.upper()} @{datetime.now()}')
        await asyncio.sleep(1)
        await websocket.send(f'{message.upper()[::-1]} @{datetime.now()}')
        await asyncio.sleep(1)
        await websocket.send(f'Length: {len(message)} @{datetime.now()}')

async def main():
    async with websockets.serve(echo, host="", port=80):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())