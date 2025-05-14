def count_characters(text):
    text = text.replace(" ", "")  # Remove all spaces
    char_count = {}

    for char in text:
        char_count[char] = char_count.get(char, 0) + 1

    return char_count

user_input = input("Say anything: ")
result = count_characters(user_input)
print("Character counts:", result)