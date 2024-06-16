
user_input = input("Enter a list of numbers separated by spaces: ")
numbers_str = user_input.split()
total_sum = 0
for num_str in numbers_str:
    total_sum += int(num_str)
print("The sum of the numbers is:", total_sum)
