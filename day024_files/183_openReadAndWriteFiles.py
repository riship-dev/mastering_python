'''
# Opens in read mode by default 
with open("test.txt") as file:
    content = file.read()
print(content)
'''

# Write mode truncates text before writing
with open("test.txt", "w") as file:
    file.write("Hello world")

# Append mode does not truncate text before writing.
with open("test.txt", "a") as file:
    file.write("\nHello world 2")