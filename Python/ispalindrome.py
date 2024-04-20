def is_palindrome(word):
    normal_word = []
    reversed_word = []
    special_characters = [" ", ",", ".", "?", "'", "!", ":"]

    # Remove the special characters by adding only letters from the alphabet
    for i in word:
        if i not in special_characters:
            normal_word.append(i)

    # Reverse the word and do the same
    for i in word[::-1]:
        if i not in special_characters:
            reversed_word.append(i)
    
    # Join the list to a string so it can be compared
    normal_word = ("".join(normal_word)).lower()
    reversed_word = ("".join(reversed_word)).lower()
    
    # Compare the two words
    if normal_word == reversed_word:
        return "Is a palindrome"
    else:
        return "Isn't a palindrome"
    
while True:
    a = input("Write a palindrome: ")
    if a == "exit()":
        break

    print(is_palindrome(a))