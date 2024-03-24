import socket
from threading import Thread


def handle_connection(client, address):
    print(f"Connected to client {address}")
    while True:
        res = client.recv(1024)
        if not res:
            break
        print(f"Recieved message '{res.decode('utf-8')}' from client {address}")
        client.send(b"ack\n")
    client.close()


def run_webserver(host: str, port: int):
    listening_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listening_socket.bind((host, port))
    listening_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listening_socket.listen()
    threads = []
    try:
        while True:
            t = Thread(target=handle_connection, args=listening_socket.accept()) # <------ new
            t.start() # <------- new
            threads.append(t)
    except KeyboardInterrupt:
        print("Closing server")
        listening_socket.close()
        for thread in threads:
            thread.join()


if __name__ == "__main__":
    run_webserver("localhost", 19991)