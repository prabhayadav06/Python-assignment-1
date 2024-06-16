
user_input = input("Enter a string: ")
title_case_string = ""
new_word = True
for char in user_input:
    if new_word and char.isalpha():
        title_case_string += char.upper()
        new_word = False
    else:
        title_case_string += char
    if char == " ":
        new_word = True
print("Title case string:")
print(title_case_string)
