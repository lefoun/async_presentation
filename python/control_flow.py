import asyncio

# Warning: This is pseudo code. It does not work.

async def handle_connection(client):
    print(f"Connected to client {client}")
    while msg := await client.read(1024):
        msg = msg.decode('utf8').strip()
        if msg[:4] == "read":
            with open(msg[3:], 'r') as f:
                asyncio.create_task(read_from_file(f, client))
        else:
            asyncio.create_task(client.write(b"ack\n"))
    print(f"Client {client} disconnected")
    client.close()

async def read_from_file(file_handle, client) -> str:
        read = await file_handle.read()
        await client.send(read)

async def run():
    server = await asyncio.start_server(handle_connection, "localhost", 19991)
    await server.serve_forever()

