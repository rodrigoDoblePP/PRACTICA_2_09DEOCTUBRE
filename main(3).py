#Codigo 1 y 2 Funcion que muestre el saludo Hey amigos! cada vez que se le pida

print("Welcome to Practica 2 Segundo Parcial!")
print (" ")
print ("Piedra Gonzlaez Rodrigo 3-W 1204")
print(" ")

def my_function():
    print("Hey amigos!")  # Imprime un saludo
    return  # Finaliza la función (aunque no es necesario aquí)

my_function() # Llama a la función para ejecutar su contenido

print(" ") #Imprime un espacio en blanco

mensaje = input("Ingresa tu nombre: ") # Solicita al usuario que ingrese su nombre y guarda el valor en 'mensaje'

print("¡Hola!,", mensaje) # Imprime un saludo personalizado utilizando el nombre ingresado
