def is_palindrome(word):
    normal_word = []
    reversed_word = []
    
    # Check each word letter and add them to a list
    for i in word:
        if i not in [" ", ",", ".", "?", "'", "!"]:
            normal_word.append(i)

    # Reverse the word and do the same
    for i in word[::-1]:
        if i not in [" ", ",", ".", "?", "'", "!"]:
            reversed_word.append(i)
    
    # Join the list to a string so it can be compared
    normal_word = ("".join(normal_word)).lower()
    reversed_word = ("".join(reversed_word)).lower()
    
    # Compare the two words
    if normal_word == reversed_word:
        return "Is a palindrome"
    else:
        return "Isn't a palindrome"
    
print(is_palindrome(input("Write a palindrome: ")))