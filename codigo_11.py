#codgio 11  Que saque la distancia dirigida entre dos puntos
print("Welcome to Practica 2 Segundo Parcial!")
print (" ")
print ("Piedra Gonzlaez Rodrigo 3-W 1204")
print(" ")


def verificar_distancia(punto1, punto2):
    # Calcula la distancia total entre dos puntos utilizando el valor absoluto
    distancia_total = abs(punto1 - punto2)  # Usa abs() para obtener la diferencia positiva
    return f"La distancia entre los dos puntos es de {distancia_total} km."  # Retorna un mensaje con la distancia

try:
    # Solicita al usuario que ingrese la distancia del primer punto y la convierte a float
    punto1 = float(input("Ingrese la distancia del punto 1 (en km): "))
    
    # Solicita al usuario que ingrese la distancia del segundo punto y la convierte a float
    punto2 = float(input("Ingrese la distancia del punto 2 (en km): "))

    # Llama a la función 'verificar_distancia' y guarda el resultado en 'resultado'
    resultado = verificar_distancia(punto1, punto2)
    
    # Imprime el resultado obtenido de la función
    print(resultado)

except ValueError:
    # Captura el error si el usuario no ingresa un valor numérico válido
    print("Por favor, ingrese valores numéricos válidos.")  # Mensaje de error para el usuario


