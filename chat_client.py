import sys
import socket
import select
 
def chat_client():
    
    # Create a TCP/IP socket
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_sock.settimeout(2)
     
    # Connect the socket to the port where the server is listening
    try :
        client_sock.connect(('localhost', 10000))
    except :
        print 'Gagal Konek'
        sys.exit()
     
    print 'Terkoneksi ke Host'
    sys.stdout.write('[Saya] '); sys.stdout.flush()
     
    while True:
        socket_list = [sys.stdin, client_sock]
         
        ready_to_read,ready_to_write,in_error = select.select(socket_list , [], [])
         
        for sock in ready_to_read:             
            if sock == client_sock:
                data = sock.recv(4096)
                if not data :
                    print '\nDiskonek'
                    sys.exit()
                else :
                    sys.stdout.write(data)
                    sys.stdout.write('[Saya] '); sys.stdout.flush()     
            
            else :
                msg = sys.stdin.readline()
                client_sock.send(msg)
                sys.stdout.write('[Saya] '); sys.stdout.flush() 

if __name__ == "__main__":

    sys.exit(chat_client())
