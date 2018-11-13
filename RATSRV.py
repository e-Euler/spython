import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 7615
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(5)
print"[*] Listening on %s:%d" % (bind_ip, bind_port)


def sendmsg(client_socket):
    command=""
    while command != "exit":
        try:
            command = raw_input()
            if (command == "disconnect"):
                client_socket.close()
                server.close()
                exit()
            elif ("switch" in command):
              client_socket = command.partition(" "[2])
            else:
              client_socket.send(command)
        except Exception as e:
            print "Connection lost %s" % (addr[0],)


def listen(client_socket):
    while True:
        results = client_socket.recv(4096)
        print"[%s] Sent: \n%s" % (addr[0], results)


while True:
    print "Starting Server...."
    client, addr = server.accept()
    print "[*] Connection Accepted from %s:%d" % (addr[0], addr[1])
    send = threading.Thread(target=sendmsg, args=(client,))
    hear = threading.Thread(target=listen, args=(client,))
    send.start()
    hear.start()
