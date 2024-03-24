import asyncio

async def handle_connection(reader, writer):
    client = writer.get_extra_info("peername")
    print(f"Connected to client {client}")
    while msg := await reader.read(1024):
        msg = msg.decode('utf8').strip()
        print(f"Recieved message '{msg}' from client {client}")
        writer.write(b"ack\n")
        await writer.drain()
    print(f"Client {client} disconnected")
    writer.close()

async def run_server():
    server = await asyncio.start_server(handle_connection, "localhost", 19991)
    async with server:
        await server.serve_forever()

asyncio.run(run_server())