"""
#largo de palabra xd
usuario = input("palabra: ")

print(len(usuario))

#calcula radio del circulo


import math

usuario = int(input("ingrese el radio del circulo: "))

pi = math.pi

radioCir = pi*usuario**2

print("el area es: ", radioCir) 

usuario = int(input("Ingrese su edad: "))

if usuario >= 18 and usuario <= 100:
    print("puede pasar")
else:
    print("se queda pringaoo")

dolar = 45
euro = 50

# convertidor de moneda euro y dolar a uy

moneda = input("seleccione que moneda quiere convertir: ")
monto = int(input("que monto: "))

if moneda.strip().lower() == "dolar":
    print(monto * dolar)
elif moneda.strip().lower() == "euro":
    print(monto * euro)
else:
    print("moneda equivocada") """

#conversion pulgada a cm


usuario_cm = float(input("porfavor ingrese el numero en centimetros a convertir a pulgadas: "))

pulgada_to_cm = 0.393701

conversion = pulgada_to_cm * usuario_cm

print("la conversion de ", usuario_cm, " a pulgadas es: ", conversion)

