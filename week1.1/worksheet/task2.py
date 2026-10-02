"""
Portfolio Task - Week 1
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: Adnan Khan
"""

name = input("What is your name? ")
print(f"Welcome to LeedsBank's savings calculator {name}!")

# Ask the user to input an amount they want to save every month - this should be an integer.
# Validate that they have entered an integer.
try:
       amount_1 = int(input("Enter the amount you want to save every month: "))
       yearly_total_amount = amount_1 * 12
       print(f"you will save £{yearly_total_amount} by the end of this year")
       interest = yearly_total_amount * 0.008 
       final_amount = yearly_total_amount + interest
       print(f"You will save £{final_amount:.2f} with interest by the end of this year")

except ValueError:
       print("Please enter an integer only")


# Calculate the total amount of money they will have saved by the end of the year (amount per month multiplied by 12).
# print this out for the user with a suitable message.


# Calculate the total amount of money including interest (0.8% of the final annual amount) they will have saved in a year.
# print this out in the format £X.XX (to two decimal places).

