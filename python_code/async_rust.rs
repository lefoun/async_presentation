async fn coroutine() -> i32 {
    println!("Hello world!");
    let result = add_two(1, 2).await;
    let x = get_x();
    return result;
}

async fn add_two(one: i32, two: i32) -> i32 {
    return one + two;
}

fn wait_on_coor() {
    block_on(|| {
        let future: Future<i32> = coroutine();  // this has the necessary size
        while true {
            match future.poll() {
                future::Ready(val) => println!("The future is complete with value {val}"),
                future::Waiting => println!("The future is waiting. Keep pollin'!"),
            };
        }
    });
}