import random
 
words = ["life", "home"]
 
print("Hangman Game")
 
while True:
    new_game = input("New Game?(y/n)")
    
    if new_game == "y":
        word = [i for i in random.choice(words)]
        correct_word = ["_" for i in range(len(word))]
        wrong_letters = []
        
        # Will loop until the user get the correct word
        while True:
            guess = input(":")
            
            for letter in word:
                if guess == letter and letter not in correct_word:
                    correct_word[word.index(letter)] = guess
                
            if guess not in word and guess not in wrong_letters:
                wrong_letters.append(guess)
                   
            print(" ".join(correct_word))
            print(", ".join(wrong_letters))
            
            # Break loop if user got correct word
            if correct_word == word:
                break
                
            if len(wrong_letters) > 6:
                print("You lose!")
                break
    else:
        break
    
