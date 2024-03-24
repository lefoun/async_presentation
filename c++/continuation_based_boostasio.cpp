#include <boost/asio.hpp>

#include <iostream>

void foo(auto socket, auto buffer) {
    auto continuation = [](auto bytes_read, auto err) {
        std::cout << "async_write completed execution!\n";
    };
    boost::asio::async_write(socket, buffer, continuation);

    // This will execute before we finish writing into the socket.
    std::cout << "Finished calling async write!\n";
}
