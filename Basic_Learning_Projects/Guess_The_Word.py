import random

easy_words = ["Shoe", "Door","Moon", "Spider", "Snow", "Shirt", "Cookie", "Candy",
              "Pizza","Eyes"]

medium_words = ["Television","Sandwich", "Aeroplane","Banana", "Rainbow", "Grapes",
                "Coffee","Mermaid","Student","Vacation"]

difficult_words = ["Octopus","Sleepover","Imagination","Sunscreen","Dictionary","Closet","Dripping","Hibernation",
                   "Homeless","Bookshelf"]


print("Welcome to the word guessing gamee")
difficulty_level= input("Please enter the difficulty level (e for easy/ m for medium / h for hard): ").strip().lower()

if difficulty_level == "e" or difficulty_level == "m" or difficulty_level == "h":
    if difficulty_level == "e":
        secret_word = random.choice(easy_words)
        secret_word_lower=secret_word.strip().lower()
    elif difficulty_level == "m":
        secret_word = random.choice(medium_words)
        secret_word_lower = secret_word.strip().lower()
    elif difficulty_level == "h":
        secret_word = random.choice(difficult_words)
        secret_word_lower = secret_word.strip().lower()
else:
    print("Sorry, the difficulty level entered  is incorrect. Please enter 'e' for easy/ 'm' for medium / 'h' for hard")


attempts=0

while True:
    user_guess=input("Please enter a guess: ").strip().lower()
    attempts=attempts+1

    if user_guess == secret_word_lower:
        print(f"Congratulations!!!!!You guessed the word in {attempts} attempts!")
        break

    hint=""
    for i in range(len(secret_word_lower)):
        if i<len(user_guess) and user_guess[i]==secret_word_lower[i]:
            hint+=user_guess[i]
        else:
            hint+="_"
    print("Hint : "+hint)

print("Over!")





