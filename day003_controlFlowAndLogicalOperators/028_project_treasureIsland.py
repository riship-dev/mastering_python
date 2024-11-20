def treasureIsland():
    print("Welcome to Treasure Island.\nYour mission is to find the treasure")
    
    decision1 = input("left or right?: ")
    if decision1 == "right":
        print("Fall into a hole.\nGame Over.")
        return
    
    decision2 = input("swim or wait?: ")
    if decision2 == "swim":
        print("Attacked by trout.\nGame Over.")
        return
    
    decision3 = input("Which door [red, blue, yellow]?: ")
    if decision3 == "red":
        print("Burned by fire.\nGame Over.")
        return
    if decision3 == "blue":
        print("Eaten by beasts.\nGame Over.")
        return
    print("You win")

treasureIsland()