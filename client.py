import asyncio
import websockets


async def main():
    async with websockets.connect('ws://localhost:8001') as ws:
        while True:
            msg = input('Enter message:')
            if msg == 'quit':
                ws.close()
                break
            await ws.send(msg)
            result = await ws.recv()
            print('> ', result)

asyncio.run(main())
