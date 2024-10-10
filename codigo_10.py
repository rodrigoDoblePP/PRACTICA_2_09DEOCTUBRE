#codigo 10   Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario
# devuelve Falso

print("Welcome to Practica 2 Segundo Parcial!")
print (" ")
print ("Piedra Gonzlaez Rodrigo 3-W 1204")
print(" ")

def validacion(vocal):
    return vocal in ('a', 'e', 'i', 'o', 'u')

while True:
    vocal = input("Ingresa una letra para verificar si es una vocal: ")
    if validacion(vocal):
        print("True. Es una vocal")
        break
    else:
        print("Falso. No es una vocal. Vuelve a ingresar una letra.")