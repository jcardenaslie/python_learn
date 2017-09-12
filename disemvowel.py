def disemvowel(word):
    list_word = list(word)
    new_word = []
    for letter in list_word:
        l = letter.lower()
        if l != 'a' and l != 'e' and l != 'i' and l != 'o' and l != 'u':
            new_word.append(letter)
    word = ''.join(new_word) 
    return word

def disemvowel2(word):
    list_word = list(word)
    new_word = []
    for letter in list_word:
        l = letter.lower()
        if l == 'a' or l == 'e' or l == 'i' or l == 'o' or l == 'u':
            list_word.remove(letter)
    word = ''.join(list_word) 
    return word

word = "joaquin"
new_word = disemvowel(word)
print(new_word)