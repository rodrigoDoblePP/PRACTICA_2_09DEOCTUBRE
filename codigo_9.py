#codigo 9 Escribir una funcion sum() y una función multip() que sumen y multipliquen respectivamente
#todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4])
#debería devolver 24.

print("Welcome to Practica 2 Segundo Parcial!")
print (" ")
print ("Piedra Gonzlaez Rodrigo 3-W 1204")
print(" ")

def suma_y_multiplicacion():
    # Lista de números
    lista = [1, 2, 3, 4]
    
    # Calcula la suma y la multiplicación en un solo paso
    suma = sum(lista)  # Usa la función sum() para obtener la suma de la lista
    multiplicacion = 1  # Inicializa el total de multiplicación
    for num in lista:
        multiplicacion *= num  # Multiplica cada número de la lista
    
    return suma, multiplicacion  # Retorna ambos resultados

# Ejecución y resultados
resultado_suma, resultado_multiplicacion = suma_y_multiplicacion()  # Llama a la función y descompone los resultados

# Imprime los resultados
print("Suma de la lista:", resultado_suma)
print("Multiplicación de la lista:", resultado_multiplicacion)
