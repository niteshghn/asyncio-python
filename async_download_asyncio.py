import asyncio
from timeit import default_timer

import aiohttp


async def fetch(session, url):
    print('starting this at', default_timer())
    async with session.get(url) as response:
        return await response.text()

async def main():
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
        base_url = "https://people.sc.fsu.edu/~jburkardt/data/csv/"
        csvs_to_fetch = [
            "ford_escort.csv",
            "cities.csv",
            "hw_25000.csv",
            "mlb_teams_2012.csv",
            "nile.csv",
            "homes.csv",
            "hooke.csv",
            "lead_shot.csv",
            "news_decline.csv",
            "snakes_count_10000.csv",
            "trees.csv",
            "zillow.csv"
        ]
        futures = [fetch(session,base_url+file) for file in csvs_to_fetch]
        start_time = default_timer()
        data = await asyncio.gather(*futures)
        print('time_taken===', default_timer()-start_time)
        # print(data)

if __name__ == '__main__':
    asyncio.run(main())