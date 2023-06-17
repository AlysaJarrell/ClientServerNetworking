# Overview

This is a basic TCP client-server network, I wrote this to further my understanding about networks and sockets. 

It is a client-server program, it is written so that as soon as a client opens it tries to connect with the server. For that reason you will want to open (through cmd) TCPServer.py first, followed by the TCPClient.py file 3 times (in separate cmds).* 

*You could do less clients but you would need to comment or get rid of the code corresponding with the other clients in TCPServer in order for it to run properly.

As client connections are made to the server, server will print out the address that it is connected to. Once all three clients are connected you can begin. As of right now the server will only listen for the next client in sequential order, when three has sent it will again be ready for one. This means that clients can send a message out of order, but it will not be received by the server or be responded to until the prior clients send and receive their message(s). The server takes the message received, turns it into all uppercase letters and sends it back. This is simply to demonstrate the server receiving a unique message, doing something with it and responding. 


[Software Demo Video](https://www.youtube.com/watch?v=Jr3EuGpEOOo)

# Network Communication

Client/Server 

I used TCP and a random port number (6677)

Takes a sentence (input) as a string, encodes it in Bytes according to ascii and decodes from ascii.

# Development Environment

Programmed in Python 3.8.6 64-bit

Libraries: socket, sys

Wrote and edited code in Visual Studio Code.
Ran code through separate cmd windows.

# Useful Websites

* [Python Networking- Tutorials Point](https://www.tutorialspoint.com/python/python_networking.htm)
* [Network Programming Beginners (overview)](https://internalpointers.com/post/network-programming-beginners-overview)


# Future Work

* I would love to make a way the server can work with which ever client sends a message (in that moment rather than it waiting on other clients before getting a response). As far as I understand this would take threading which I haven't been able to get into yet. 
* I would also like to try to implement something where the clients could talk to each other through the server. For example, client 1 would send something, the server receives it and sends it to client 2 and vice versa. This should be as simple as changing where the server sends the modified message.
* I also need to set up a way that when a single client 'quits' it will close all of the clients and the server's sockets.
