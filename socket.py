import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the host and port to listen on
host = '127.0.0.1'  # Use your server's IP or '0.0.0.0' to listen on all available network interfaces
port = 8080

# Bind the socket to the host and port
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(5)

print(f"Server listening on {host}:{port}")

while True:
    # Accept a connection from a client
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address}")

    # Receive data from the client
    data = client_socket.recv(1024).decode('utf-8')
    values = data.split(',')
    
    if len(values) == 3:
        try:
            # Convert received values to integers and calculate the sum
            num1 = int(values[0])
            num2 = int(values[1])
            num3 = int(values[2])
            result = num1 + num2 + num3

            # Send the result back to the client
            response = f"HTTP/1.1 200 OK\r\n\r\n{result}"
            client_socket.send(response.encode('utf-8'))
        except ValueError:
            response = "HTTP/1.1 400 Bad Request\r\n\r\nInvalid input values"
            client_socket.send(response.encode('utf-8'))
    else:
        response = "HTTP/1.1 400 Bad Request\r\n\r\nInvalid input format"
        client_socket.send(response.encode('utf-8'))

    # Close the client socket
    client_socket.close()

# Close the server socket
server_socket.close()