"""3.-Crear un programa en el cual, Ingrese 10 valores,y proceda a calcular su suma y promedio."""

sum=0
for i in range(10):
    num = int(input(f"Ingrese el numero {i+1} :  "))
    sum = sum + num

prom = sum/10

print("La suma de los numeros es : ", sum)
print("El promedio de los numeros es : ", prom)

print("PROGRAMA FINALZIADO!!")
