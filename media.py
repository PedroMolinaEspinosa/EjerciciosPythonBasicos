print("------------------------------------------")
print("Vamos a hacer la media de números introducidos hasta que escribas exit\n\n")
introducido = ''
numeros = []
while introducido != "exit":
    if introducido == "exit":
        break
    else:
        introducido = float(input('Introduce un numero: \n'))
        
        numeros.append(introducido)

media = 0
float(media)
for numero in numeros:
    media = media + numero
media = media / len(numeros)
print(media)
    

 