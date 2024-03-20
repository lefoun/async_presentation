async def get_forty_two() -> int:
    return 42


async def foo() -> int:
    print("Hello world! I'm an async function!")
    answer = await get_forty_two()
    return answer
