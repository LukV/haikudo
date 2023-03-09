import asyncio
from api import call_api
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--topic', type=str, required=True)
parser.add_argument('--mood', type=str, required=False, default="Happy")
args = parser.parse_args()

async def run_api():
    response = await call_api(args.topic, args.mood)
    print(response)


async def main():
    await run_api()


if __name__ == '__main__':
    asyncio.run(main())