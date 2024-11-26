#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./input/letters/starting_letter.txt") as starting_letter:
    content = starting_letter.read()

with open("./input/names/invited_names.txt") as invited_names:
    names = invited_names.readlines()
names = [name.strip() for name in names]

for name in names:
    with open(f"./output/ReadyToSend/{name}.txt", "w") as starting_letter:
        email = content.replace("[name]", name)
        starting_letter.write(email)
