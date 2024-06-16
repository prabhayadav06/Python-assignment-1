
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

string1 = string1.replace(" ", "").lower()
string2 = string2.replace(" ", "").lower()

char_count1 = {}
char_count2 = {}

for char in string1:
    if char in char_count1:
        char_count1[char] += 1
    else:
        char_count1[char] = 1

for char in string2:
    if char in char_count2:
        char_count2[char] += 1
    else:
        char_count2[char] = 1

if char_count1 == char_count2:
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
