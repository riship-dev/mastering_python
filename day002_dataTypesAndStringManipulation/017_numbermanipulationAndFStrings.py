# Make float look presentable
bmi = 84 / 1.65 ** 2
print(int(bmi)) # Floors the number
print(round(bmi)) # Mathematically rounds the number
print(round(bmi, 2)) # Rounds float to 2 decimal spaces

# Assignment operators
number = 100
number += 10 # 90
number -= 10 # 100
number *= 10 # 1000
number /= 10 # 100

# f strings
name = "Rishi"
print(f"Hi {name}")