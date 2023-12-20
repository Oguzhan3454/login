import socket

input_ip = input("İp adresini giriniz: ")
# İstemci konfigürasyonu
HOST = input_ip
PORT = 8080

# Socket oluştur
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# Veri gönder
message = "Merhaba, bu bir test mesajıdır."
client_socket.send(message.encode())

# Bağlantıyı kapat
client_socket.close()
