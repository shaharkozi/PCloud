from ast import Bytes
import socket
import requests

HOST = "localhost"
PORT = 7000

# basic function calls the model
def CPUUtil():
    number = 28
    return '{ "name":"John", "age":30, "city":"New York"}' 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024) # recive the String from the Client
            if not data:
                break
            Result = CPUUtil()
            req
            conn.sendall(bytes(b'{ "value":"True" }')) # the result from the model

# if __name__ == "__main__":
#     main()
