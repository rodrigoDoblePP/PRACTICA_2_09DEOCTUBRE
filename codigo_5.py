#Codigo 5 Calcular el área de un círculo  y el volumen 
#otra que calcule el volumen de un cilindro y utilice  primera función.
print("Welcome to Practica 2 Segundo Parcial!")
print (" ")
print ("Piedra Gonzlaez Rodrigo 3-W 1204")
print(" ")
import math  # Importa la librería 'math' para usar funciones matemáticas, como pi

radio = float(input("¿Cual es el radio ?\n"))  # Pide al usuario que ingrese el radio y lo convierte a un número decimal

def area(radio):
    # Calcula el área de un círculo usando la fórmula π * radio²
    return math.pi * (radio ** 2)

def volumen(h):
    # Calcula el volumen de un cilindro usando el área de la base * altura
    return area(radio) * h

op = input("Deseas obtener (1)Area o (2) Volumen ")  # Pide al usuario que elija entre calcular el área (1) o el volumen (2)

if op == "1":
    print(area(radio))  # Si elige '1', llama a la función 'area' y muestra el resultado
elif op == "2":
    h = float(input("¿Cual es la altura:? "))  # Si elige '2', pide la altura, la convierte a float y llama a 'volumen'
    print(volumen(h))  # Imprime el resultado del volumen

