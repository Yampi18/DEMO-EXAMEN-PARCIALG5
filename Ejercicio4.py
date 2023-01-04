"""4.-Introduce una contraseña, en la cual si no es la contraseña correcta,
Intruso, introduce la contraseña correcta, y si es la correcta
Que resalte en la pantalla Contraseña correcta."""

contraseña = str(input("Ingrese la contraseña: "))
if contraseña == "unfv2023":
    print("Contraseña correcta")
else:
    print("Intruso")