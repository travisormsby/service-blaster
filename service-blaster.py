import aiohttp
import asyncio
import sys

async def request_urls(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.ensure_future(get_url(session, url)) for url in urls]
        return await asyncio.gather(*tasks)

async def get_url(session: aiohttp.ClientSession, url: str):
    async with session.request("GET", url, verify_ssl=False) as response:
        return await response.text()
    
if __name__ == "__main__":
    url = sys.argv[1]
    reqs = int(sys.argv[2])
    urls = [url] * reqs
    responses = asyncio.run(request_urls(urls))
    print(responses[0])