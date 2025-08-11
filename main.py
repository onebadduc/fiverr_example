from function import bank
from function import calculate_income
from function import budget
def main():
    i = 5
    while i != 4:
        print("Please select a program to run by typing the corresponding number")
        print("1. Bank")
        print("2. Calculate Income")
        print("3. Budgeting")
        print("4. Exit")
        i = int(input("Press Enter after selection: "))
        if i == 1:
            bank()
        elif i == 2:
            calculate_income()
        elif i == 3:
            budget()
        


main()