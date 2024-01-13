import socket
port=12345
host='0.0.0.0'
def receive_file(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()

        print(f"Server listening on {host}:{port}")

        connection, address = server_socket.accept()
        print(f"Connected by {address}")

        file_data = b''
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            file_data += data

        with open('received_file.txt', 'wb') as file:
            file.write(file_data)

        print("File received successfully")
receive_file(port,host)
    
