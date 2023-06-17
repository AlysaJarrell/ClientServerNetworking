
# This is TCPClient.py

from socket import *

# serverName tells us what computer (ip address) in the world to send our packet to.
# serverName is the "ip address" of the server we will send too, this could be changed
# serverPort tells us what application on that computer to go to (specifies between google chrome and zoom); it gets it to the right program
serverName = 'localhost'    # you could also use '127.0.0.1' which IS the localhost, (keeps it on this computer) 
serverPort = 6677           # I assigned a random port number (it is the same as I listed for the DEFALT_PORT in SERVER) 



# define a socket type; more information in TCPServer.py comments
clientSocket = socket(AF_INET, SOCK_STREAM)

# connect() connects to a computer, it also creates and binds a socket on your machine but the values are random/not needed. it'll stay as long as 
# the handshake doesn't close
clientSocket.connect((serverName, serverPort)) #(ip address, port)
sentence = '' 

while True:
   sentence = input('Input lowercase sentence: ')   # gets input from client

   if sentence == 'quit':                           # check if wanting to "quit"/close socket
      clientSocket.send(sentence.encode('ascii'))   # encodes and sends quit to server so it can close as well
      break                                         # breaks while loop and jumps to line 34 and closes socket
   
   clientSocket.send(sentence.encode('ascii'))      # encodes the letters/charcters into bytes to send and will later be decoded back through ascii
   print("Sentence sent to change to upper case: ", sentence)

   modifiedSentence = clientSocket.recv(1024).decode('ascii')  #recv()s will accept 1024 bytes which should large enough for these purposes
   print("From Server: ", modifiedSentence)

print("Closing Connection, Closing Program")        # prints closing warning
clientSocket.close()                                # closes client socket