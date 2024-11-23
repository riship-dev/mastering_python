name = "Rishi" # Global scope

def print_name():
    name = "not Rishi" # Local Scope
    print(name)

print_name()
print(name)