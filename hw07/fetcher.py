"""
Simple fetcher to asynchronous get requests
"""
import asyncio
import sys
import aiohttp


FILE = None


async def fetch(pid, url):
    """
    Gets server name of given url via get request
    """
    print("Fetch async process {} started".format(pid))
    await asyncio.sleep(0)
    async with aiohttp.request("GET", url) as response:
        server = response.headers.get("Server")
        response.close()
        return [url, server]


def next_url(file):
    """
    Reads next url from file
    """
    i = 0
    while True:
        url = file.readline()
        if not url:
            break
        url = url.replace("\n", "")
        yield i, url
        i += 1
    file.close()


async def main(loop, count_of_workers, f):
    """
    Run asynchronous fetching
    """
    tasks = []
    result = {}
    for i, url in next_url(f):
        if len(tasks) == count_of_workers:
            tmp = await asyncio.gather(*tasks)
            for res in tmp:
                result[res[0]] = res[1]
            tasks = []
        tasks.append(loop.create_task(fetch(i + 1, url)))
    tmp = await asyncio.gather(*tasks)
    for res in tmp:
        result[res[0]] = res[1]
    print(result)
    return result


if __name__ == '__main__':
    workers_count = int(sys.argv[1])
    file_name = sys.argv[2]
    FILE = open(file_name, "r")
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(main(event_loop, workers_count, FILE))
    event_loop.close()
