import socket
import asyncio


def handle_connection(client, address) -> bool:
    """Returns True to close the connection."""
    res = client.recv(1024)
    if not res:
        print(f"Client {address} disconnected")
        client.close()
        return True
    msg = res.decode('utf-8').strip()
    print(f"Recieved message '{msg}' from client {address}")
    client.send(b"ack\n")
    return False


def run_webserver(host: str, port: int):
    listening_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listening_socket.bind((host, port))
    listening_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listening_socket.setblocking(False) # <------- new
    listening_socket.listen()
    sockets_to_read = {listening_socket: listening_socket.getsockname()} # <------- new
    try:
        while True:
            readables, _, _ = select.select(sockets_to_read.keys(), [], [])  # <--------- new
            for readable_socket in readables:
                if readable_socket == listening_socket:
                    client, address = listening_socket.accept()
                    print(f"Connected to client {address}")
                    client.setblocking(False)
                    sockets_to_read[client] = address # <--------- new
                else:
                    close_connection = handle_connection(readable_socket, sockets_to_read[readable_socket]) # <------- new
                    if close_connection:
                        del sockets_to_read[readable_socket]
    except KeyboardInterrupt:
        print("Closing server")
        listening_socket.close()


if __name__ == "__main__":
    run_webserver("localhost", 19991)