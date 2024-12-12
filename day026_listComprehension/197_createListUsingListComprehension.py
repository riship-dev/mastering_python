a = [1, 2, 3]
a_plus_1 = [num + 1 for num in a]
print(a_plus_1)

b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [num for num in b if num % 2 == 0]
print(even_numbers)

c = [num * 2 for num in range(0, 10)]
print(c)