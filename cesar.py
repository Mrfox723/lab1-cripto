def cifrado_cesar(texto, desplazamiento):
    resultado = ""
    for caracter in texto:
        if caracter.isalpha():  # Solo cifrar letras
            ascii_offset = 65 if caracter.isupper() else 97
            nuevo_caracter = chr(((ord(caracter) - ascii_offset + desplazamiento) % 26) + ascii_offset)
            resultado += nuevo_caracter
        else:
            resultado += caracter  # No cifrar caracteres especiales ni espacios
    return resultado

# Pedir texto y desplazamiento
mensaje = input("Ingrese el texto a cifrar: ")
desplazamiento = int(input("Ingrese el desplazamiento: "))

# Cifrar el mensaje
mensaje_cifrado = cifrado_cesar(mensaje, desplazamiento)
print(f"Texto cifrado: {mensaje_cifrado}")

# Al final de cesar.py, después de imprimir el resultado
with open("mensaje_cifrado.txt", "w") as archivo:
    archivo.write(mensaje_cifrado)
