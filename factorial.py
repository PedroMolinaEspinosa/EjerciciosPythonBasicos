print("Vamos a hacer el factorial del numero introducido\n\n")

introducido = 0
introducido = int(input("Introduce el número para la operación factorial: \n"))
factorial = 1
for numero in range(1,introducido+1):
    factorial *= numero

print("El número factorial de", introducido," es ",factorial )
