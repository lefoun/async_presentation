async function get_forty_two(): Promise<number> {
    return 42;
}

async function foo(): Promise<number> {
    console.log("Hello world! I'm an async function!");
    const answer = await get_forty_two();
    return answer;
}