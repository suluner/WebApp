import orm
from models import User, Blog, Comment

import asyncio
import sys


async def test(loop):
    await orm.create_pool(loop=loop, user='www-data', password='www-data', db='awesome')
    u = User(name='Test', email='test6@example.com', passwd='123456789', image='about:blank')
    await u.save()

loop = asyncio.get_event_loop()
task = asyncio.ensure_future(test(loop))
loop.run_until_complete(task)
loop.close()
if loop.is_closed():
    sys.exit(0)
