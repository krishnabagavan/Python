print("WELCOME TO TREAURE ISLAND")
print("YOUR MISSION IS TO FIND THE TREASURE")
krishna=input("you are at cross road.were do you want to go LEFT OR RIGHT:\n")
if krishna=='Left':
    choose=str(input("you came to lake.there is an island in the middle of the lake.type 'WAIT' to wait for a boat.type 'SWIM' to swim across.:\n"))
    if choose=='wait':
          check=input("you arrive at the island.there is a house with 3 doors.one RED(R), ONE YELLOW(Y),ONE BLUE(B):\n")
          if check=='R':
            print("burn")
          elif check=='Y':
              print("you enter room waste.'GAME OVER'")
          else:
              print("CONGRATS:'YOU WON THE GAME'")
    else:
        print("GAME OVER")
else:
    print("Game Over")

     