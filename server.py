import socket
import sys

# Create a socket object for TCP/IP communication
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server address and port
server_address = ('localhost', 8080)
print('Starting up the server on {} port {}'.format(*server_address))

# Bind the socket to the server address and port
sock.bind(server_address)

# Set the socket to listen for incoming connections
sock.listen(1)

# Start an infinite loop to handle incoming connections
while True:
    print('Waiting for a client to connect...')
    connection, client_address = sock.accept()

    # Define the valid username and password
    username = 'admin'
    password = 'admin123'

    try:
        print('Connection from', client_address)

        # Start a loop to receive data from the client
        while True:
            data = connection.recv(1024)
            if data:
                # If received data is username
                if data.decode() == username:
                    # Wait to receive password
                    data = connection.recv(1024)
                    if data.decode() == password:
                        print('AUTH_SUCCESS')
                        # Send an authentication success message to the client
                        connection.sendall('AUTH_SUCCESS'.encode())

                        # Start a chat session
                        while True:
                            # Receive messages from the client
                            data = connection.recv(1024)
                            if data:
                                print('Received {!r}'.format(data))
                                if data.decode().lower() == 'stop':
                                    print('Chat session ended by the client.')
                                    break
                                # Send the same message back to the client
                                connection.sendall(data)
                            else:
                                break
                    else:
                        print('AUTH_FAIL')
                        # Send an authentication failure message to the client
                        connection.sendall('AUTH_FAIL'.encode())
                        break
                else:
                    print('AUTH_FAIL')
                    # Send an authentication failure message to the client
                    connection.sendall('AUTH_FAIL'.encode())
                    break
                    
            else:
                print('No data from', client_address)
                break
            
    finally:
        # Close the connection
        connection.close()

