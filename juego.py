
import random


numero_secreto = random.randint(0,100)
#print(numero_secreto)
cant_intentos = 0
max_intentos = 5
adivinado = False

print("bienvenido al juego")

while not adivinado and cant_intentos < max_intentos:
    entrada = int(input("Introduce el num: ")) #convertir a num
    numero = entrada
    if numero == numero_secreto:
        print("ganaste")
        adivinado = True
    elif numero < numero_secreto:
        print("numero mayor")
    else:
        print("numero menor")
    cant_intentos += 1

    if not cant_intentos < max_intentos:
        print("perdiste")