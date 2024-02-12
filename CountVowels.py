def count_vowels(word):
    #vowels
    vowels = {'a', 'e', 'i', 'o', 'u'}


    vowel_count = 0


    for char in word:

        char_lower = char.lower()

        if char_lower in vowels:
            vowel_count += 1

    return vowel_count

input_word = input("Enter a word: ")
num_vowels = count_vowels(input_word)
print("Number of vowels:", num_vowels)

