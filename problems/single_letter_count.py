# define single_letter_count below:
def single_letter_count(word, letter):
    letter = letter.lower()
    word = word.lower()
    if letter in word:
        return word.count(letter)
    return 0


print(single_letter_count("word here hehehe", "h"))
print(single_letter_count("word here hehehe", "o"))
print(single_letter_count("word here hehehe", "z"))
