/*C4.- programa para hallar el factorial de un numero ingresado por el usuario*/ 

var factorial =1
var num=Number(prompt("Ingrese un numero: "))
for(var i=1;i<=num;i++){
    factorial=factorial*i
}

window.alert("El factorial de "+num+" es igual a : "+factorial)