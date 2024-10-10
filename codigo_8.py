#codiog 8 Definir una función (), que tome tres números como argumentos y devuelva el
#mayor de ellos.
print("Welcome to Practica 2 Segundo Parcial!")
print (" ")
print ("Piedra Gonzlaez Rodrigo 3-W 1204")
print(" ")

def mayor_de_tres_numeros(a, b, c):
    # Compara a con b y c para determinar el mayor
    if a >= b and a >= c:
        return a  # Retorna a si es mayor o igual que b y c
    elif b >= a and b >= c:
        return b  # Retorna b si es mayor o igual que a y c
    else:
        return c  # Si no se cumple ninguna de las condiciones anteriores, retorna c

num1 = int(input("Ingresa el primer número: "))  # Pide al usuario el primer número y lo convierte a entero
num2 = int(input("Ingresa el segundo número: "))  # Pide al usuario el segundo número y lo convierte a entero
num3 = int(input("Ingresa el tercer número: "))  # Pide al usuario el tercer número y lo convierte a entero

mayor = mayor_de_tres_numeros(num1, num2, num3)  # Llama a la función para obtener el mayor de los tres números
print(f"El número mayor es: ", mayor)  # Imprime el resultado
