#Codigo 7 Función que de un string, regrese la longitud de la última palabra. Las palabras tienen separación por uno o más espacios.
print("Welcome to Practica 2 Segundo Parcial!")
print (" ")
print ("Piedra Gonzlaez Rodrigo 3-W 1204")
print(" ")

def longitud_ultima_palabra(frase):
    # Divide la frase en palabras y devuelve la longitud de la última
    return len(frase.strip().split()[-1]) if frase.strip() else 0

# Ejemplo de uso
frase = input("Introduce una frase: ")  # Solicita al usuario una frase
print(f"La longitud de la última palabra es: {longitud_ultima_palabra(frase)}")  # Imprime la longitud de la última palabra
