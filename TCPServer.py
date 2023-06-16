
# This is TCPServer.py

import sys
from socket import *


# create a value that will be the port number
DEFAULT_PORT = 6677

#this just checks if the port entered is a real int, can be deleted
serverPort = int(sys.argv[1]) if len(sys.argv) == 2 else DEFAULT_PORT

# define a socket type socket_stream specifies TCP. 
serverSocket = socket(AF_INET, SOCK_STREAM)

# Actually bind the socket to the OS. This now makes the socket valid and usable.  the port is now in use
serverSocket.bind(('', serverPort))

# listen is waiting for someone to TCP handshake with. 
serverSocket.listen(1)  #the parameters are how many handshakes we want to have at once

print('The Server is ready to receive')
connectionSocket, addr = serverSocket.accept()   # here we are accepting a handshake. A socket is created per handshake to communicate with that 
                                                 # specific connection and the ip address to resend back to. a socket is needed for every in and out packet.

print(f"Connected: {addr}")     # shows what address we are connected to 
print("\n")

try:
   while 1:
      sentence = connectionSocket.recv(1024).decode('ascii')   # using this socket, we recv() a message (it will wait until it gets one)

      if sentence == 'quit':            # if server receives 'quit' from Client we will close the socket on the server side
         connectionSocket.close()       # closes the connection socket (the handshake)
         print(f"Closed Connection with: {addr}")
         break                          # breaks while loop
      
      print ("Received from client:", sentence) # prints the message on server side
      capitalizedSentence = sentence.upper()    # modifies sentence to be all uppercase
      connectionSocket.send(capitalizedSentence.encode('ascii')) # Sends the message back encoded (in Bytes)


   print("Closing Server")

except KeyboardInterrupt:
   print("\nClosing Server")
   serverSocket.close()     # closes the server socket
