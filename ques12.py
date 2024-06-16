number = input("Enter a number: ")
sum = 0
for digit_char in number: 
    digit = int(digit_char)
    sum += digit
print(f"The sum of the digits of the number is: {sum}")
