# Original list
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print("Original List:", my_list)

# 1. Basic Slicing: Extracting a sublist
print("\n1. Basic Slicing:")
print("From index 2 to 5 (exclusive):", my_list[2:5])  # [30, 40, 50]

# 2. Omitting start index (starts from 0)
print("\n2. Omitting Start Index:")
print("From the start to index 3 (exclusive):", my_list[:3])  # [10, 20, 30]

# 3. Omitting end index (goes to the end)
print("\n3. Omitting End Index:")
print("From index 5 to the end:", my_list[5:])  # [60, 70, 80, 90, 100]

# 4. Slicing with step
print("\n4. Slicing with Step:")
print("Every second element from index 1 to 7:", my_list[1:8:2])  # [20, 40, 60, 80]

# 5. Negative Indexing
print("\n5. Negative Indexing:")
print("Last 3 elements:", my_list[-3:])  # [80, 90, 100]
print("Sublist from index -5 to -2 (exclusive):", my_list[-5:-2])  # [60, 70, 80]

# 6. Reversing a List
print("\n6. Reversing a List:")
print("Reversed List:", my_list[::-1])  # [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]

# 7. Copying the Entire List
print("\n7. Copying the Entire List:")
print("Copy of the List:", my_list[:])  # [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# 8. Skipping Elements
print("\n8. Skipping Elements:")
print("Every third element:", my_list[::3])  # [10, 40, 70, 100]

# 9. Reverse with Specific Range
print("\n9. Reverse Specific Range:")
print("Elements from index 8 to 3 in reverse:", my_list[8:2:-1])  # [90, 80, 70, 60, 50]