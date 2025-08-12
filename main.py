from function import payments
from function import calculate_income
from function import budget
def main():
    i = 5
    while i != 4:
        print("Please select a program to run by typing the corresponding number")
        print("1. Payments")
        print("2. Calculate Income")
        print("3. Budgeting")
        print("4. Exit")
        i = int(input("Press Enter after selection: "))
        if i == 1:
            payments()
        elif i == 2:
            calculate_income()
        elif i == 3:
            budget()
        if i != 4:
            print("would you like to make another selection?")
            r = input("y/n: ")
            if r == "n":
                i = 4

        


main()