import asyncio
import websockets


async def handler(websocket):
    while True:
        try:
            message = await websocket.recv()
            print('Message received from client :', message)
            await websocket.send('Message from server: ' + message)
        except Exception as e:
            print(e)
            break


async def main():
    async with websockets.serve(handler, 'localhost', 8001):
        await asyncio.Future()


if __name__ == '__main__':
    asyncio.run(main())

