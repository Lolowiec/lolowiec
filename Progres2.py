

import socket   

if __name__ == "__main__":
    ip = "127.0.0.1"
    port= 1234
    
    server = socket.socket(socket(socket.AF_INET, socket.SOCK_STREAM))
    server.bind((ip, port))
    server.listen(5)
    
    while True:
        client, Address = server.accept()
        print(f"Conection - {addres[0]} : {addres[1]} ") 