size = input("Size? [S, M, L]: ")
pepperoni = input("Pepperoni? [Y, N]: ")
extraCheese = input("Extra cheese? [Y, N]: ")

cost = 15

if size == "M":
    cost += 5
elif size == "L":
    cost += 10

if pepperoni == "Y":
    cost += 2

if extraCheese == "Y":
    cost += 1

print(f"Cost = {cost}$")