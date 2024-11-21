import random

randomWords = ["apple", "banana", "mountain", "river", "sky", "ocean", "forest", "dream", "cloud", "spark"]
randomWord = random.choice(randomWords)
userProgress = ["_" for _ in randomWord]
lives = 6

while lives > 0:
    print(f"\nLives = {lives}")
    print(" ".join(userProgress))
    playerGuess = input("Guess a letter: ")

    if playerGuess in randomWord:
        print(f"{playerGuess} exists.")
        for idx, letter in enumerate(randomWord): #learn?????????
            if letter == playerGuess:
                userProgress[idx] = playerGuess
    else:
        lives -= 1
        print(f"{playerGuess} does not exist.")

    if "_" not in userProgress:
        print("\nYou won!")
        print("The word was:", randomWord)
        break
else:
    print("\nYou lost!")
    print("The word was:", randomWord)