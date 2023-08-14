# %%


# %%

# We put the whole code into a while loop to get words from the user indefinitely.
while True:
    word = input("Enter a word ('quit' to exit): ")
    if word.lower() == "quit":
        break

    # We set an empty dictionary, then check whether each letter is alphabet or not,
    # then we add the letter with its number occurrences in the dict
    letter_count = {}
    for letter in word:
        if letter.isalpha():
            letter_count[letter] = letter_count.get(letter, 0) + 1

    # Here we get the most number of a letter is repeated.
    max_count = 0
    if letter_count:
        max_count = max(letter_count.values())
    else:
        max_count = 0

    # Here we get the most frequent letter with using the most occurred item.
    most_frequent_letters = []
    for letter, count in letter_count.items():
        if count == max_count:
            most_frequent_letters.append(letter)

    # We check whether the most frequent letters is the most of the most occurred letters,
    # if not, no letter is changed with the given symbol.
    if len(most_frequent_letters) == 1:
        most_frequent_letter = most_frequent_letters[0]
        replaced_word = word.replace(most_frequent_letter, "@")
    else:
        unique_letters = set(letter_count.keys())
        for letter in unique_letters:
            if letter_count[letter] == max_count:
                replaced_word = word
                break
        else:
            most_frequent_letter = most_frequent_letters[0]
            replaced_word = word.replace(most_frequent_letter, "@")

    print("\nReplaced word:", replaced_word)
    if replaced_word != word:
        print("Original word:", word, "\n")
