def payments():
    print("Choose which type of payments to calculate")
    print("1. Set Payments")
    print("2. Payment Amount")
    i = int(input())
    if i == 1:
        amount_of_payments = float(input("Total payment installments: "))
        total_cost = float(input("Total to be paid: "))
        cost_per_payment = total_cost / amount_of_payments
        print("***PAYMENT REPORT***")
        print(f"Total Payments: {amount_of_payments:.0f}")
        print(f"Cost Per Payment: {cost_per_payment:.2f}")
        print("***END REPORT***")
    elif i == 2:
        total_cost = float(input("Total to be paid: "))
        cost_per_payment = float(input("Amount paid per month: "))
        amount_of_payments = total_cost / cost_per_payment
        print("***PAYMENT REPORT***")
        print(f"Total Payments: {amount_of_payments:.0f}")
        print(f"Cost Per Payment: {cost_per_payment:.2f}")
        print("***END REPORT***")
    else:
        print("Error returning to main menu")
        print("Please choose a number listed")


def calculate_income():
    fed_tax = 0.12
    pay_per_hour = float(input("Enter pay per hour: "))
    hour_worked = float(input("Enter hours worked this pay period: "))
    gross_pay = pay_per_hour * hour_worked
    take_home = gross_pay - (gross_pay * fed_tax)
    print("***PAY REPORT***")
    print(f"Pay before tax is: {gross_pay}")
    print(f"Pay after federal tax is: {take_home}")
    print("***END REPORT***")


def budget():
    period = input("Enter budget period in format(m/d-m/d): ")
    pay_this_period = float(input("Enter amount to budget: "))
    money_not_budget = pay_this_period
    bills = float(input("Enter total amount in bills due: "))
    money_not_budget -= bills
    print(f"Money left to budget: ${money_not_budget}")
    savings = float(input("Enter amount to put into savings: "))
    money_not_budget -= savings
    print(f"Money left to budget: ${money_not_budget}")
    food_cost = float(input("Enter estimate of food cost this period: "))
    money_not_budget -= food_cost
    print(f"Money left to budget: ${money_not_budget}")
    other = float(input("Enter amount you plan on spending on non-essentials: "))
    print(f"***BUDGET FOR ${period}")
    print(f"Total Bills: ${bills}")
    print(f"Total to Save: ${savings}")
    print(f"Estimate food cost: ${food_cost}")
    print(f"Other costs: ${other}")
    if money_not_budget > 0:
        print(f"Money left over: ${money_not_budget}")
    print("***END OF BUDGET***")
    with open("budget_report", "a") as file:
        file.write("\n")
        file.write(f"***BUDGET FOR ${period}\n")
        file.write(f"Total Bills: ${bills}\n")
        file.write(f"Total to Save: ${savings}\n")
        file.write(f"Estimate food cost: ${food_cost}\n")
        file.write(f"Other costs: ${other}\n")
        if money_not_budget > 0:
            file.write(f"Money left over: ${money_not_budget}\n")
        file.write("***END OF BUDGET***\n")

