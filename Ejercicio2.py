"""2.-Generar un programa, en el cual, nos asignen una pregunta, y de contestar mal, 
Aparecerá respuesta errónea."""

print('''***MENU DE PREGUNTAS***
Opcion 1 : Cultura general
Opcion 2 : Matematica
Opcion 0 : Salir
''')

opc=3

while opc != 0 :

    opc = int(input('Elija una opcion: '))

    if opc== 1 :
        num1 = int(input("¿Cuantos dias tiene un año bisiesto? "))
        if num1 == 366:
            print("Respuesta correcta") 
        else:
            print("Respuesta incorrecta")         
        
    elif opc== 2 :
        num2 = int(input("¿Cuantos primos hay entre 0 y 50? "))
        if num2 == 15:
            print("Respuesta correcta") 
        else:
            print("Respuesta incorrecta")    

print("PROGRAMA FINALIZADO")

    

    

        

   