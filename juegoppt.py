player1 = input("piedra papel o tijera?: ")
player2 = input("piedra papel o tijera?: ")

if player1 == player2:
    print("Empate")
elif (player1 == "piedra" and player2 == "tijera") or (player1 == "papel" and player2 == "piedra") or (player1 == "tijera" and player2 == "papel"):
    print("player 1 gana")
else:
    print("player 2 gana")