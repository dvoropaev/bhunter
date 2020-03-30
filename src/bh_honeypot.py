#!/usr/bin/env python3
import socket, sys, threading, paramiko
# from threading import Thread

#generate keys with 'ssh-keygen -t rsa -f server.key'
# HOST_KEY = paramiko.RSAKey(filename='./server.key')
SSH_PORT = 22

def honeypot(source, client_socket):
    HOST_KEY = paramiko.RSAKey(filename='./server.key')
    class SSHServerHandler (paramiko.ServerInterface):
        def __init__(self):
            self.event = threading.Event()
        def check_auth_password(self, username, password):
            print("New login: {}:{}:{}".format(source[0], username, password))
            return paramiko.AUTH_FAILED
        def get_allowed_auths(self, username):
            return 'password'

    transport = paramiko.Transport(client_socket)
    transport.add_server_key(HOST_KEY)
    server_handler = SSHServerHandler()
    transport.start_server(server=server_handler)
    channel = transport.accept(1)
    if not channel is None:
        channel.close()

def main():
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind(('', SSH_PORT))
        server_socket.listen(100)

        # paramiko.util.log_to_file ('paramiko.log')

        while(True):
            try:
                client_socket, client_addr = server_socket.accept()
                threading.Thread(target=honeypot, args=(client_addr, client_socket,)).start()
                # thread.start_new_thread(handleConnection,(client_socket,))
            except Exception as e:
                print("ERROR: Client handling")
                print(e)

    except Exception as e:
        print("ERROR: Failed to create socket")
        print(e)
        sys.exit(1)

main()
