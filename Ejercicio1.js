/*1.-Realiza un programa en el cual, si se ingresa un número 
que esté entre el rango del 3 al 12, el programa volverá a pedir
Que se ingrese un número, hasta que se detecte un número fuera del rango.*/

var num=Number(prompt("ingrese un numero"));


while(num>=3 && num<=12){
    var num=Number(prompt("ingrese un numero"));
    window.alert("El numero esta en el rango, ingrese otro nuemero fuera del rango");
    

}
window.alert("El numero esta fuera del rango");