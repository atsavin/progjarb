import sys
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    	# Wait for a connection
    	print >>sys.stderr, 'waiting for a connection'
    	connection, client_address = sock.accept()
    	print >>sys.stderr, 'connection from', client_address
    	# Receive the data in small chunks and retransmit it
    	while True:
        	data = connection.recv(1000)
        	print >>sys.stderr, 'received "%s"' % data
            	if data:
                	#print >>sys.stderr, 'sending data back to the client'
			            #content = urllib2.urlopen("home.html")
                	connection.send('HTTP/1.1 200 OK\n')
			            connection.send('Content-Type: text/html\n')
			            connection.send('\n')
            			connection.send("""<html>
            					   <body>
            					   <h1>Rijal Web</h1>
            					   Selamat datang di Server Rijal
            					   </body>
            					   </html""")
            			#connection.sendall("Host: 127.0.0.1\n\n")
            			#connection.sendall("Content-Type: text/html; charset=UTF-8\n\n")
            	else:
                	print >>sys.stderr, 'no more data from', client_address
                	break
        # Clean up the connection
	connection.close()
