/* 3.-Crear un programa en el cual, Ingrese 10 valores, 
y proceda a calcular su suma y promedio.
*/

var sum=0

for( var i=0;i<10;i++){
    var num=Number(prompt("Ingrese el numero "+ (i+1)+ ": "))
    sum=sum+num;

}

var prom=sum/10

window.alert(" La suma de los numeros es: "+ sum +"\n El promedio de los numero es: "+prom)
