cadena = input('Introduce una cadena o palabra: ')

inversion = ''
for caracter in cadena:
    inversion = caracter + inversion
if cadena == inversion:
    print("Es palindromo illo")
else:
    print("No es palindromo acho")

