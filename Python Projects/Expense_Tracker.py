print("="*50)
print("            PERSONAL FINANCE TRACKER")
print("="*50)
print("Track your monthly income and expenses!")
print("Get insights into your spending habits.")
print("\n")

print("PERSONAL INFORMATION")
print("*"*50)
name = input("Enter your full name: ")
age = int(input("Enter your age: "))
savings_account = input("Do you have a savings account(yes/no): ")
financial_goal = input("Your financial goal: ")
print("\n")


print("INCOME DETAILS")
print("="*50)
main_sal = int(input("Enter your main job salary: "))
side_income = int(input("Enter your side income: "))
other_income = int(input("Enter your other incomes: "))
print("\n")

print("MONTHLY EXPENSES")
print("="*50)
rent = int(input("Enter your rent: "))
food = int(input("Enter your expense for food and groceries: "))
transportation = int(input("Enter your expense for transportation: "))
entertainment = int(input("Enter your expense for entertainment: "))
utilities =  int(input("Enter your expense for utilities: "))
misc_expenses = int(input("Enter your expense for miscellanious expense: "))
print("\n")

total_income = main_sal+side_income+other_income
total_expense = rent+food+transportation+entertainment+utilities+misc_expenses

monthly_savings = total_income-total_expense
savings_rate = (monthly_savings/total_income)*100
expense_ratio = (total_expense/total_income)*100

rent_per = (rent/total_expense)*100
food_per = (food/total_expense)*100
trans_per = (transportation/total_expense)*100
entertain_per = (entertainment/total_expense)*100
utilities_per = (utilities/total_expense)*100
misc_per = (misc_expenses/total_expense)*100
expense_per = (total_expense/total_expense)*100

saving_money = monthly_savings > 0
overspending = total_income < total_expense
emergency_buffer = monthly_savings >= (total_expense*3)
high_income_earner = total_income > 20000
high_entertainament_spending = entertain_per > 20

debt_to_income_ratio = (total_expense/total_income)*100
food_budget_ratio= (food/total_income)*100
entertainment_bedget_ratio = (entertainment/total_income)*100

print("="*50)
print("FINANCIAL REPORT")
print("="*50)
print("\n")
 
print("🙍‍♂️USER PROFILE")
print("Name: ",name)
print("Age: ",age," years old")
print("Has Savings Account: ", savings_account)
print("Financial Goal: ", financial_goal)
print("\n")

print("💰INCOME BREAKDOWN")
print("Main Salary: Rs.",main_sal)
print("Side Income: Rs.",side_income)
print("Other Income: Rs.",other_income)
print("Total Monthly Income: Rs.",total_income)
print("Projected Annual Income: Rs.",total_income*12)
print("\n")

print("💸EXPENSE BREAKDOWN")
print(f"Rent: Rs.{rent:,.2f} ({rent_per:.1f}% of total expenses)")
print(f"Food: Rs.{food:,.2f} ({food_per:.1f}% of total expenses)")
print(f"Transport: Rs.{transportation:,.2f} ({trans_per:.1f}% of total expenses)")
print(f"Entertainment: Rs.{entertainment:,.2f} ({entertain_per:.1f}% of total expenses)")
print(f"Utilities: Rs.{utilities:,.2f} ({utilities_per:.1f}% of total expenses)")
print(f"Miscellanious: Rs.{misc_expenses:,.2f} ({misc_per:.1f}% of total expemses")
print("Total Monthly Expenses: Rs.",total_expense)
print("\n")

print("🪙SAVINGS ANALYSIS:")
print(f"Monthly Savings: {monthly_savings:,.2f}")
print(f"Projected Annual Savings: {monthly_savings*12:,.2f}")
print(f"Savings Rate: {savings_rate:.1f}%")
print(f"Expense Ratio: {expense_ratio:.1f}%")
print("\n")

print("🧧FINANCIAL HEALTH CHECK:")
print("Saving Money: ",saving_money)
print("Overpending: ",overspending)
print("Has emergency buffer: ", emergency_buffer)
print("High Income Earner: ",high_income_earner)
print("High Entertainament Spending: ",high_entertainament_spending)
print("\n")

print("FINANCIAL RATIOS:")
print(f"Debt-to-income Ratio: {debt_to_income_ratio:.1f}%")
print(f"Food Budget Ratio: {food_budget_ratio:.1f}%")
print(f"Entertainment Budget Ratio: {entertainment_bedget_ratio:.1f}%")

print("\n"+"="*60)
print("            PROJECT SUMMARY")
print("=" * 60)

print(f"Dear {name}, based on your financial data:")
print(
    f"You earn Rs.{total_income:,.2f} monthly"
    f" and spend Rs.{total_expense:,.2f}."
)

