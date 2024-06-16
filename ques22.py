
user_input = input("Enter a list of numbers separated by spaces: ")

numbers_str = user_input.split()
numbers = [int(num) for num in numbers_str]
if len(numbers) > 0:
    min_value = numbers[0]
    max_value = numbers[0]
else:
    min_value = None
    max_value = None

for num in numbers:
    if num < min_value:
        min_value = num
    if num > max_value:
        max_value = num
        
if min_value is not None and max_value is not None:
    print("The minimum value is:", min_value)
    print("The maximum value is:", max_value)
else:
    print("The list is empty.")
