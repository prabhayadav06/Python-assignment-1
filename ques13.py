birth_year = int(input("Enter your birth year: "))
import datetime
current_year = datetime.datetime.now().year
age = current_year - birth_year
print(f"You are {age} years old.")
