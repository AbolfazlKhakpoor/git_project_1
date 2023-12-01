
player1 = input("player 1 , Please Enter sang , kaghaz or gheychi")
player2 = input("player 2 , Please Enter sang , kaghaz or gheychi")

if player1 == "sang" and player2 == "gheychi":
    print("player 1 win")
elif player1 == "gheychi" and player2 == "sang":
    print("player 2 win")
elif player1 == "kaghaz" and player2 == "sang":
    print("player 1 win")
elif player1 == "sang" and player2 == "kaghaz":
    print("player 2 win")
elif player1 == "gheychi" and player2 == "kaghaz":
    print("player 1 win")
elif player1 == "kaghaz" and player2 == "gheychi":
    print("player 2 win")
elif player1 == "sang" and player2 == "sang":
    print("tie")
elif player1 == "gheychi" and player2 == "gheychi":
    print("tie")
elif player1 == "kaghaz" and player2 == "kaghaz":
    print("tie")







