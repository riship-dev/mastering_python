'''
- A dictionary is a collection of key-value pairs in Python. Keys are unique, and each key maps to a specific value.
- Keys must be immutable: Keys can be strings, numbers, or tuples, but not mutable types like lists.
- Values can be of any type: Values can be integers, strings, lists, other dictionaries, or any valid Python object.
- From Python 3.7 onward, dictionaries maintain the insertion order of keys.
- Add a new key-value pair or update an existing key:
    my_dict["key3"] = "value3"  # Add
    my_dict["key1"] = "new_value"  # Update
- Use del or pop() to remove items:
    del my_dict["key1"]
    removed_value = my_dict.pop("key2")
- Use loops to iterate through keys, values, or both:
    for key in my_dict:
        print(key, my_dict[key])
    for key, value in my_dict.items():
        print(key, value)
- Common methods include:
    dict.keys() - Returns all keys.
    dict.values() - Returns all values.
    dict.items() - Returns key-value pairs as tuples.
    dict.get(key, default) - Safely gets a value, avoiding KeyError.
'''

definitions = {
    "bug": "An error in a program that prevents the program from running as expected.",
    "algorithm": "A step-by-step procedure or formula for solving a problem.",
    "debugging": "The process of identifying and removing errors from a program.",
    "variable": "A named storage location in memory that holds a value which can change during program execution.",
    "function": "A block of organized, reusable code that performs a specific task."
}

print(definitions["bug"])