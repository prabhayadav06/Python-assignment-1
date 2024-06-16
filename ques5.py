string_input = input("Enter a string: ")

with open("C:/Users/PRABHA/OneDrive/Documents/New folder/fordemo.txt",'w') as file:
    file.write(string_input)
print("The string has been written to file")