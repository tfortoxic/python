#new 
from datetime import date
try:
    year = int(input("Enter your birth year: "))
    month = int(input("Enter your birth month in number: "))
    day = int(input("Enter the day of the month you were born: "))

    birth_year = date(year, month, day)
    todays_date = date.today()

    if birth_year <= todays_date:
        age = todays_date.year - birth_year.year
        print("You are ", age ,"years old")
    else:
        print("Invalid input: Birthdate is in the future.")

except ValueError:
    print("Invalid input: Please enter valid numbers for year, month, and day.")

except OverflowError:
    print("Invalid input: The provided values are too large.")

except Exception as e:
    print("An error occurred:", e)
		

