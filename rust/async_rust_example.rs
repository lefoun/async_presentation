use tokio::runtime::Runtime;
use tokio::task;

use std::thread;
use std::time::Duration;

async get_password(db: Database) -> String {
    return db.get_password().await;
}

async get_name(db: Database) -> String {
    return db.get_name().await;
}

fn main() {
    let database = create_database();

    // Creates the event loop.
    let runtime = Runtime::new().unwrap();

    // Equivalent to loop.run_until_complete(asyncio.wait(tasks)) in python
    runtime.block_on(async move {
        let name = await get_name(database);
        let password = await get_password(database);
        println!("The name of admin is {name} and their password is {password}!");
    });
}
