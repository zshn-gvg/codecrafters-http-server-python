# Uncomment this to pass the first stage
import socket


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    #
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    # server_socket.accept() # wait for client
    connection, address = server_socket.accept()
    data = connection.recv(1024)
    response = "HTTP/1.1 200 OK\r\n\r\n"
    connection.sendall(response.encode())
    connection.close()

if __name__ == "__main__":
    main()
