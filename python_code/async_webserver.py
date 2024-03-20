import socket
import select


class RegisterType:
    READ = 0
    WRITE = 1


class Task:
    def __init__(self, socket: socket):
        self._socket = socket


class EZSocket:
    def __init__(self, socket: socket):
        self._socket = socket
        self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._socket.setblocking(False) # Important
    
    def bind(self, *args):
        self._socketbind(*args)
    
    def listen(self):
        self._socket.listen()
    
    async def accept(self) -> AsyncGenerator[Task, None, None]:
        yield (self._socket, RegisterType.READ)
        return Task(self._socket.accept())



class EventLoop:
    def __init__(self):
        self._tasks: list[Task] = []
        self._need_to_read: list[Task] = []
        self._need_to_write: list[Task] = []
        self._read: list[Task] = []
    
    def register_io(self, task: Task, register_type: RegisterType):
        pass
    
    def run(self):
        while True:
            readables, writables, _ = select.select(self._need_to_read, self._need_to_write, [])
            for readable in readables:
                pass


_event_loop = EventLoop()


def get_event_loop() -> EventLoop:
    return _event_loop


if __name__ == '__main__':
    pass


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