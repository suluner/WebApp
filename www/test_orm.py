from orm import *
import asyncio

class User(Model):
    __table__ = 'user'
    id = IntegerField(primary_key=True)
    name = StringField()

async def main(loop):
    await create_pool(loop, **database)
    user = User(id=125, name='Huting')
    await user.save()
    user1 = await user.find(125)
    return user1

database = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'ht0881654',
    'db': 'school'
}

loop = asyncio.get_event_loop()
task = asyncio.ensure_future(main(loop))
res = loop.run_until_complete(task)
print(res)
