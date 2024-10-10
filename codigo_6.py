#- Capturar dirección de email. Desplegar mensaje si la dirección es válida o no, siendo que una función lo revisar por tener la @ solo así es valida
print("Welcome to Practica 2 Segundo Parcial!")
print (" ")
print ("Piedra Gonzlaez Rodrigo 3-W 1204")
print(" ")

def es_email_valido(email):
    return '@' in email  # Verificar si el email contiene el carácter '@'

email_usuario = input("Ingresa tu dirección de email: ") # Capturar la dirección de email del usuario

if es_email_valido(email_usuario): # Verificar si la dirección es válida y mostrar el mensaje correspondiente
    print("La dirección de email es válida.")  #Imprime si la direccion de email es valida
else:
    print("La dirección de email no es válida.") #imprime si la direccion de email no es valida
