import asyncio
from datetime import datetime, timezone
from dateutil.relativedelta import relativedelta
from prisma import Client
import logging
logging.basicConfig()

async def main():
    logging.getLogger('prisma').setLevel(logging.DEBUG)
    client = Client()
    await client.connect()
    today = datetime.now(timezone.utc)
    print(await client.demo.find_many(where={
        'created_at': {
            'lt': today
        }
    }))
    print(await client.demo.find_many(where={
        'created_at': {
            'lte': today
        }
    }))
    print(await client.demo.find_many(where={
        'created_at': {
            'gt': today
        }
    }))
    print(await client.demo.find_many(where={
        'created_at': {
            'gte': today
        }
    }))
    print(await client.demo.find_many(where={
        'created_at': {
            'gt': datetime(year=today.year, month=today.month, day=today.day),
            'lt': today + relativedelta(day=1),
        }
    }))
    print(await client.demo.find_many(where={
        'created_at': {
            'gt': today + relativedelta(day=1),
            'lt': datetime(year=today.year, month=today.month, day=today.day)
        }
    }))
    print(await client.demo.find_many(where={
        'AND': [
            {
                'created_at': {
                    'lt': today + relativedelta(day=1),
                }
            },
            {
                'created_at': {
                    'gt': datetime(year=today.year, month=today.month, day=today.day)
                }
            }
        ]
    }))
    print(await client.demo.find_many(where={
        'AND': [
            {
                'created_at': {
                    'gt': today + relativedelta(day=1),
                }
            },
            {
                'created_at': {
                    'lt': datetime(year=today.year, month=today.month, day=today.day)
                }
            }
        ]
    }))

asyncio.run(main())
