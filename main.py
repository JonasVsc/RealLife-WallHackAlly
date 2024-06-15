import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 5000))  # Escutando na porta 5000
    server_socket.listen(5)
    print("Server listening on port 5000")

    while True:
        client_socket, address = server_socket.accept()
        print(f"Connection from {address} has been established!")
        client_handler(client_socket)

def client_handler(client_socket):
    with client_socket:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"Received data: {data.decode('utf-8')}")

if __name__ == "__main__":
    start_server()
