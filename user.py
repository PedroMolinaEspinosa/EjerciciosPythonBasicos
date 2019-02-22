import re
print("Validación de usuario introducido por teclado \n\n")
print("--------------------------------------------------")

regex = '^[a-zA-Z_]+$'
nombre = input("Introduce el nombre de usuario\n")
if re.match(regex,nombre):
    print("correcto")
else:
    print("No, zoquete!")