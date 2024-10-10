#Calcular total de una factura luego del IVA. 
#primero obtener la cantidad sin IVA 
#luego el porcentaje de IVA a aplicar, 
#por ultimo devolver el total de la factura. 
print("Welcome to Practica 2 Segundo Parcial!")
print (" ")
print ("Piedra Gonzlaez Rodrigo 3-W 1204")
print(" ")

def calcular_factura(cantidad_sin_iva, iva=21): # Calcula el total sumando el IVA a la cantidad sin IVA

    total = cantidad_sin_iva + (cantidad_sin_iva * iva / 100)  #Total de la factura
    return total  # Retorna el total con IVA incluido

cantidad = float(input("Escribe la cantidad sin IVA: "))  # Pido al usuario la cantidad sin IVA y la convierto a float
iva = input("Escribe el porcentaje de IVA (o presiona Enter para usar 21%): ")  
# Pregunto el porcentaje de IVA, o presiono enter para usar el 21%

if iva: # Verifico si el usuario ingresó un porcentaje de IVA
    iva = float(iva)  # Si se ingresa un IVA, lo convierto a número (float)
    total = calcular_factura(cantidad, iva)  # Calculo el total con el IVA ingresado
else:
    total = calcular_factura(cantidad)  # Si no ingresó nada, uso el 21



