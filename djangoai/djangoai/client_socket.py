import socket

def send_query_to_socket_server(pregunta):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 8080))
    client.send(pregunta.encode())
    from_server = client.recv(4096)
    client.close()
    return from_server.decode()
