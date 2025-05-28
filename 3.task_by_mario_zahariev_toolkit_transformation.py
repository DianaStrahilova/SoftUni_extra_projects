# 🧵 Python Text Transformation Toolkit

# Step 1: Display a menu to the user
print("🧠 Welcome to the Text Transformation Toolkit!")
print("Choose a transformation:")
print("1. Reverse Text")
print("2. Convert to Uppercase")
print("3. Convert to Lowercase")
print("4. Title Case")
print("5. Count Vowels")
print("6. Remove All Spaces")
print("7. Replace Vowels with '*'")
print("8. Check if Palindrome")
print("9. Word Frequency Counter")

# Step 2: Get the user's choice
choice = int(input("Enter the number corresponding to your choice: "))

# Step 3: Get the input string
text = input("Enter the text: ")

# Step 4: Apply the selected transformation
if choice == 1:
    # TODO: Reverse the text using slicing or a loop
    reversed_word = text[::-1]
    print(reversed_word)

elif choice == 2:
    # TODO: Convert the text to uppercase using string methods
    capitalised_word = text.upper()
    print(capitalised_word)

elif choice == 3:
    # TODO: Convert the text to lowercase using string methods
    lower_case_word = text.lower()
    print(lower_case_word)

elif choice == 4:
    # TODO: Convert the text to title case (capitalize each word)
    capitalised_words = text.capitalize()
    print(capitalised_words)

elif choice == 5:
    # TODO: Count how many vowels are in the text (a, e, i, o, u)
    vowels = "a, e, i, o, u"
    vowels_count = 0
    word = text.lower()

    for letter in vowels:
        if letter in word:
            vowels_count += 1
    print(vowels_count)

elif choice == 6:
    # TODO: Remove all spaces from the string using replace() or join()
    text = text.replace(" ", "")
    print(text)

elif choice == 7:
    # TODO: Replace all vowels with "*" using a loop or comprehension
    new_text = ""

    for vowels in text:
        if vowels.lower() in "aeiou":
            new_text += "*"
        else:
            new_text += vowels

    print(new_text)


elif choice == 8:
    # TODO: Check if the text is a palindrome (ignoring case and spaces)
    text = text.lower().replace(" ", "")

    if text == text[::-1]:
        print("Text is a palindrome!")
    else:
        print("Text is not a palindrome.")


elif choice == 9:
    # TODO: Count the frequency of each word and display the result
    text = text.lower().split()
    freq = {}

    for word in text:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    for word, count in freq.items():
        print(f"{word}:{count}")

else:
    print("❌ Invalid choice! Please restart the program.")