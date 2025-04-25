'''Write a Python program that calculates the difference between two dates provided by a user.
Scenario Example:
A user wants to find out how many days they've lived by inputting their birthdate and today's date.
Your program should:
• Take two dates as input (format: dd-mm-yyyy).
• Output the difference in days clearly.
'''

from datetime import datetime
def get_date_input(n):
    while True:
        user = input(n)
        try:
            return datetime.strptime(user, "%d-%m-%Y").date()
        except:
            print("Invalid date format.")
# dd-mm-yyyy format
birth_date = get_date_input("Enter your birthdate:")
current_date = get_date_input("Enter today's date:")
difference = current_date-birth_date 
print(f"\nYou have lived for {difference.days} days.")