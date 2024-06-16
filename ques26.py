
user_string = input("Enter a string: ")
prefix = input("Enter a prefix to check: ")
suffix = input("Enter a suffix to check: ")

if user_string.startswith(prefix):
    print(f"The string '{user_string}' starts with the prefix '{prefix}'.")

if user_string.endswith(suffix):
    print(f"The string '{user_string}' ends with the suffix '{suffix}'.")
