def count_characters(sentence):
    alphabet_count = 0
    digit_count = 0
    space_count = 0

    for char in sentence:
        if char.isalpha():
            alphabet_count += 1
        elif char.isdigit():
            digit_count += 1
        elif char.isspace():
            space_count += 1

    return alphabet_count, digit_count, space_count

user_sentence = input("Enter a sentence: ")

alphabet_count, digit_count, space_count = count_characters(user_sentence)

print(f"Alphabets: {alphabet_count}")
print(f"Digits: {digit_count}")
print(f"Spaces: {space_count}")
