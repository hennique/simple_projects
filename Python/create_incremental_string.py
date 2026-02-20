# This function will take a string and reacreate it incrementally
# If you, for example, give it the string "Hello, World!"
# it will return "H He Hel Hell Hello Hello, Hello, W Hello, Wo Hello, Wor Hello, Worl Hello, World Hello, World!"

def create_incremental_string(text):
    final_text = []

    for i in range(1, len(text)+1):
        if text[i-1] == " ":
            continue
        
        final_text.append(text[0:i])

    return " ".join(final_text)
