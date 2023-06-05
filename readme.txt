TalkByte Protocol Implementation
This repository contains the Python implementation of the TalkByte Protocol, a simple, stateful communication protocol. The protocol involves a client-server model, in which the client sends a message to the server after authenticating the user's credentials, and the server echoes back the same message to the client.

This README serves as a guide on how to compile, build, and run the software on a Linux-based OS( I have used Ubuntu OS).

Prerequisites
Make sure that you have Python3, and pip installed on your system. 

How to Compile and Run the code

You can download the scripts and run them directly instead of  going through the cloning repository procedure( just a personal preference :) ).

You can run the server script by using the following command:
python3 server.py
After running this command, the server starts and waits for a client to connect.

Run the client script:
Open a new terminal window,  and run the client script:
python3 client.py
The client script prompts you to enter your username and password. Enter 'admin' for username and 'admin123' for password.



Send messages from the client:
Once authenticated, you can now send messages from the client. Enter your message when the client prompts "Enter your message:". The server will echo back your message.

To stop the chat session, simply type 'stop'.

Configuration and Command Line Arguments

The server and client scripts are set to run on IP address 'localhost' and port 8080 by default. If you want to change the IP address or port, you will need to update it manually in both scripts.

In server.py, change the following line:
server_address = ('localhost', 8080)

In client.py, change the following line:
server_address = ('localhost', 8080)
Make sure to use the same IP address and port number in both scripts.

Troubleshooting
If you encounter an error that the address is already in use when you try to run the server script, it means that the IP address and port number are being used by another process. You can solve this issue by choosing a different port number.

Support
If you encounter any problems or need further assistance, please open an issue on this GitHub repository. 

Contribution
Contributions to improve this implementation are welcome. Please feel free to create a pull request.


Extra information:
1. Currently, password hashing has not been incorporated into this implementation due to some challenges encountered during the process. As a result, the password is shown directly as plain text. However, for future updates and improvements, there are plans to enhance the security features of this protocol, including adding password hashing.
2. And I would like to apologise for coming short of my set expectations and will continue to improve further.  
