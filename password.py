import re
print("Programa que comprueba si la contraseña introducida es válida")
print("-------------------------------------------------------------\n")
regex =  '[A-Za-z0-9@#$%^&+=]{8,}'
password = input("Introduce la contrasela a validar\n\n")
if re.match(regex, password):
    print("Contraseña bien formada")
else:
     print("Contraseña mal formada")