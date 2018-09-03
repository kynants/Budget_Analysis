'''
Design a program that asks the user to enter the amount that he or she has
budgeted for a month. A loop should then prompt the user to enter each of his
or her expenses for the month, and keep a running total. When the loop
finishes, the program should display the amount that the user is over or under
budget.
'''

budget = float(input("Enter the amount you have budgeted for a month: "))
expenses = 0
amt_used = 0
yes_or_no = 'n'

while yes_or_no.lower() not in {'y'}:
    expenses = float(input('Enter your expenses for the month: '))
    amt_used += expenses
    yes_or_no = input('Have you entered in all your expenses? y/n ')

if amt_used < budget:
    print('You are within your budget limit by: ${}'.format(budget - amt_used))
else:
    print('You are over your budget limit by: ${}'.format(amt_used - budget))