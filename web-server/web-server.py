import socket

# Basic config for socket
HOST, PORT = '', 8888

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)

#  Implementing the listener socket
print('Serving HTTP on port no %s ...' % PORT)

while True:
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(1024)
    print(request)

    message = input("What's your message?: ")
    http_response = """\
    HTTP/1.1 200 OK

    %s
    """ % message

    client_connection.sendall(bytes(http_response, 'utf-8'))
    client_connection.close()
