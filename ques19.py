import string

user_input = input("Enter a string: ")

result = ""

for char in user_input:
    if char not in string.punctuation:
        result += char
print("String without punctuation:")
print(result)
