import socket
import sys

# Create a socket object for TCP/IP communication
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server address and port
server_address = ('localhost', 8080)
print('Connecting to {} port {}'.format(*server_address))

# Connect the socket to the server's address and port
sock.connect(server_address)

try:
    # Ask the user for username
    username = input("Enter your username: ")
    # Send the username to the server
    sock.sendall(username.encode())
    
    # Ask the user for password
    password = input("Enter your password: ")
    # Send the password to the server
    sock.sendall(password.encode())
    
    # Wait to receive the authentication result from the server
    data = sock.recv(1024)
    print('Received {!r}'.format(data))
    
    # If authentication is successful
    if data.decode() == 'AUTH_SUCCESS':
        # Start a chat session
        while True:
            # Ask the user for a message
            message = input("Enter your message: ")
            # If the user types 'stop', end the chat session
            if message.lower() == 'stop':
                print('Chat session ended by user.')
                break
            # Send the message to the server
            sock.sendall(message.encode())
            
            # Wait to receive a response from the server
            data = sock.recv(1024)
            print('Received {!r}'.format(data))
    else:
        # If authentication fails, print a message
        print('Authentication failed.')

finally:
    # Close the socket
    print('Closing socket')
    sock.close()

