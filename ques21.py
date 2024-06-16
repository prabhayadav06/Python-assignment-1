
user_input_list = input("Enter a list of elements separated by spaces: ")
elements = user_input_list.split()
element_to_count = input("Enter the element to count: ")
count = 0
for element in elements:
    if element == element_to_count:
        count += 1
print(f"The element '{element_to_count}' occurs {count} times in the list.")
