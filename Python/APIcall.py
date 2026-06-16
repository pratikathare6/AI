import asyncio
import aiohttp 


async def fetch_data():
    url = 'https://jsonplaceholder.typicode.com/todos/1'

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            print('Hello World')
            print(data)

    
asyncio.run(fetch_data())
