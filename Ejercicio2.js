/*2.-Generar un programa, en el cual, nos asignen una pregunta, y de contestar mal, 
Aparecerá respuesta errónea.*/

var opc=Number(prompt('***MENU DE PREGUNTAS*** \n  Opcion 1 : Cultura general\n  Opcion 2 : Matematica\n  Opcion 0 : Salir'))


    switch(opc){

        case 1: 
            var num1=Number(prompt("¿Cuantos dias tiene un año bisiesto?"))
            if (num1 ==366){
                window.alert("Respuesta correcta")
            }
            else{
                window.alert("Respuesta incorrecta")
            }
            break;

        case 2: 
            var num2=Number(prompt("¿Cuantos primos hay entre 0 y 50?"))
            if (num2 ==15){
                window.alert("Respuesta correcta")
            }
            else{
                window.alert("Respuesta incorrecta")
            }
            break;
    }
