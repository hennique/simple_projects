def is_palindrome(word):
    normal_word = []
    reversed_word = []
    
    for i in word:
        if i not in [" ", ",", ".", "?", "'", "!"]:
            normal_word.append(i)

    # Will reverse the word
    for i in word[::-1]:
        if i not in [" ", ",", ".", "?", "'", "!"]:
            reversed_word.append(i)
    
    normal_word = ("".join(normal_word)).lower()
    reversed_word = ("".join(reversed_word)).lower()
    
    if normal_word == reversed_word:
        return "Is a palindrome"
    else:
        return "Isn't a palindrome"
    
print(is_palindrome(input("Write a palindrome: ")))