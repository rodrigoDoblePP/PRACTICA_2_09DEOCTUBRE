# Dar un entero positivo y resuelva su factorial.

print("Welcome to Practica 2 Segundo Parcial!")
print (" ")
print ("Piedra Gonzlaez Rodrigo 3-W 1204")
print(" ")

def factorial(n):
   #Calcula el factorial de un número entero positivo.
    if n == 0 or n == 1:  # Verifica si n es 0 o 1, casos base
        return 1  # Retorna 1 porque el factorial de 0 y 1 es 1
    else:
        return n * factorial(n - 1)  # Llama a la función recursivamente

# Solicitar al usuario que ingrese un número
n = int(input("Introduce un entero positivo: "))  # Convierte la entrada del usuario a un entero

# Validar que el número sea positivo
if n >= 0:  # Verifica que n sea positivo o cero
    resultado = factorial(n)  # Calcula el factorial del número
    print(f"El factorial de {n} es {resultado}.")  # Imprime el resultado
else:
    print("Por favor, introduce un entero positivo.")  # Mensaje de error si n es negativo




    
