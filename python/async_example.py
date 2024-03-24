
import asyncio


async def countdown(name, nb):
    print(f"{name} sleeping {nb}")
    await asyncio.sleep(nb)
    print(f"{name} finished sleeping")


loop = asyncio.get_event_loop()
tasks = [
    asyncio.ensure_future(countdown("A", 2)),
    asyncio.ensure_future(countdown("B", 3)),
    asyncio.ensure_future(countdown("C", 1)),
    asyncio.ensure_future(countdown("D", 4))]

loop.run_until_complete(asyncio.wait(tasks))
loop.close()


