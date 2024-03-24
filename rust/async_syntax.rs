async fn get_forty_two() -> i32 {
    return 42;
}

async fn foo() -> i32 {
    println!("Hello world! I'm an async function!");
    let answer = get_forty_two().await;
    return answer;
}