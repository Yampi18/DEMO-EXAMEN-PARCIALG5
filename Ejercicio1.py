"""1.-Realiza un programa en el cual, si se ingresa un número que esté entre el rango del 3 al 12, el programa volverá a pedir
Que se ingrese un número, hasta que se detecte un número fuera del rango"""

numero = int(input("Ingrese un numero")); 

while(numero>=3 and numero<=12):
    print("El numero esta en el rango")
    numero = int(input("Ingrese un numero"))

print("El numero ingresesado esta fuera de rango")
print("PROGRAMA TERMINADO!!!!")