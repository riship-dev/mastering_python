states = [
    "Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut",
    "Massachusetts", "Maryland", "South Carolina", "New Hampshire",
    "Virginia", "New York", "North Carolina", "Rhode Island",
    "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana",
    "Indiana", "Mississippi", "Illinois", "Alabama", "Maine",
    "Missouri", "Arkansas", "Michigan", "Florida", "Texas",
    "Iowa", "Wisconsin", "California", "Minnesota", "Oregon",
    "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
    "North Dakota", "South Dakota", "Montana", "Washington",
    "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico",
    "Arizona", "Alaska", "Hawaii"
]

# Access items
print(states[0])
print(states[-1])

# Modify item
states[0] = 12345
print(states[0])

# Add new item
states.append("qwertyuiop")
print(states[-1])

# Add multiple items
states.extend(["hello", "world"])
print(states)