print("=" * 40)
print("          WORD COUNT PROGRAM")
print("=" * 40)

text = input("Enter a sentence: ").strip()

if text == "":
    print("You didn't enter any text.")
else:
    words = text.split()

    print("\n--- Result ---")
    print("Number of words:", len(words))
    print("Number of characters:", len(text))

    # Count each word
    word_count = {}

    for word in words:
        word = word.lower()

        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    print("\nWord frequency:")

    for word, count in word_count.items():
        print(word, ":", count)