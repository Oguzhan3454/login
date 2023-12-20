import socket

# Sunucu konfigürasyonu
HOST = '192.168.63.51'  # Tüm ağlara açık
PORT = 8080       # Kullanılacak port

# Socket oluştur
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"Dinleniyor: {HOST}:{PORT}")

# Bağlantı kabul et
client_socket, addr = server_socket.accept()
print(f"Bağlantı kabul edildi: {addr}")

# Veri al ve yaz
data = client_socket.recv(1024)
print(f"Alınan veri: {data.decode()}")

# Bağlantıyı kapat
client_socket.close()
server_socket.close()
