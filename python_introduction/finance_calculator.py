# finance_calculator.py

income = 5000
expenses = 4000

monthly_savings = income - expenses
annual_savings = monthly_savings * 12
projected_savings = annual_savings + (annual_savings * 0.05)

print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings}.")
