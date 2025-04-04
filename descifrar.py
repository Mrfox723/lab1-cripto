from termcolor import colored
from nltk.corpus import words
import nltk

# Descargar el diccionario la primera vez
nltk.download('words')

# Leer el mensaje cifrado desde el archivo
with open("mensaje_cifrado.txt", "r") as archivo:
    mensaje_cifrado = archivo.read().strip()

# Función para descifrar el cifrado César con un desplazamiento dado
def descifrar_cesar(texto, desplazamiento):
    resultado = ""
    for caracter in texto:
        if caracter.isalpha():
            ascii_offset = 65 if caracter.isupper() else 97
            nuevo_caracter = chr(((ord(caracter) - ascii_offset - desplazamiento) % 26) + ascii_offset)
            resultado += nuevo_caracter
        else:
            resultado += caracter
    return resultado

# Cargar el diccionario de palabras en inglés
diccionario = set(words.words())

mejor_puntaje = 0
mejor_mensaje = ""
mejor_shift = 0

print("\nProbando posibles desplazamientos:\n")

# Probar todos los desplazamientos posibles
for i in range(1, 26):
    descifrado = descifrar_cesar(mensaje_cifrado, i)
    palabras = descifrado.split()
    coincidencias = sum(1 for palabra in palabras if palabra.lower() in diccionario)

    if coincidencias > mejor_puntaje:
        mejor_puntaje = coincidencias
        mejor_mensaje = descifrado
        mejor_shift = i

    print(f"Shift {i}: {descifrado}")

# Imprimir el mensaje más probable en verde
print("\nMensaje más probable (mayor cantidad de palabras reconocidas):")
print(colored(f"Shift {mejor_shift}: {mejor_mensaje}", "green"))
