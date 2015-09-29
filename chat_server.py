
import sys
import socket
import select

server_address = ('localhost', 10000)
SOCKET_LIST = []
RECV_BUFFER = 4096 

def chat_server():

    # Create a TCP/IP socket
    ser_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    #Bind the socket to the port
    ser_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print >>sys.stderr, 'Masuk %s port %s' % server_address
    ser_sock.bind(server_address)

    # Listen for incoming connections
    ser_sock.listen(10)

    SOCKET_LIST.append(ser_sock)
 
    while True:

        ready_to_read,ready_to_write,in_error = select.select(SOCKET_LIST,[],[],0)
      
        for sock in ready_to_read:

            if sock == ser_sock: 
                connection, client_address = ser_sock.accept()
                SOCKET_LIST.append(connection)
                print "Client (%s, %s) terkoneksi" % client_address
                 
                broadcast(ser_sock, connection, "[%s:%s] masuk ke dalam chat room\n" % client_address)
           
            else:
                try:
                    data = sock.recv(RECV_BUFFER)
                    if data:
                        broadcast(ser_sock, sock, "\r" + '[' + str(sock.getpeername()) + '] ' + data)  
                    else: 
                        if sock in SOCKET_LIST:
                            SOCKET_LIST.remove(sock)

                        broadcast(ser_sock, sock, "Client (%s, %s) diskonek \n" % client_address) 

                except:
                    broadcast(ser_sock, sock, "Client (%s, %s) offline\n" % client_address)
                    continue
    ser_sock.close()
    

def broadcast (ser_sock, sock, message):
    for socket in SOCKET_LIST:
        if socket != ser_sock and socket != sock :
            try :
                socket.send(message)
            except :
                socket.close()
                if socket in SOCKET_LIST:
                    SOCKET_LIST.remove(socket)
 
if __name__ == "__main__":

    sys.exit(chat_server())         
