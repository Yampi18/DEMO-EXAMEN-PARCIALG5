"""4)programa para hallar el factorial de un numero ingresado por el usuario"""

factorial = 1
num = int(input("Ingrese un numero : "))
for i in range(1,num+1):
    factorial = factorial * i 
    
print(f"El factorial de " , num, "es igual a : ", factorial)
