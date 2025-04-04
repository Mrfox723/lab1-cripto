from scapy.all import IP, ICMP, send
import time

# Abrimos el mensaje cifrado desde el archivo creado por cesar.py
with open("mensaje_cifrado.txt", "r") as archivo:
    mensaje = archivo.read().strip()

# IP de destino (puedes usar 8.8.8.8 o 127.0.0.1 para pruebas locales)
destino = "8.8.8.8"

print("Enviando mensaje oculto en paquetes ICMP...\n")

for letra in mensaje:
    # Crear paquete con la letra en el campo de datos (payload)
    paquete = IP(dst=destino) / ICMP() / letra
    print(f"Enviando letra: {letra}")
    send(paquete, verbose=0)  # verbose=0 para que no imprima info técnica
    time.sleep(1)  # esperar un segundo para que parezca tráfico natural
