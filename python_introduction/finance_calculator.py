# finance_calculator.py

def fmt_number(x):
    """Return integer string if whole number, otherwise trim to up to 2 decimals."""
    x = float(x)
    if x.is_integer():
        return str(int(x))
    s = f"{x:.2f}"
    # remove trailing zeros and trailing dot if any
    return s.rstrip('0').rstrip('.')

# exact prompts required by ALX
income = float(input("Enter your monthly income: "))
expenses = float(input("Enter your total monthly expenses: "))

monthly_savings = income - expenses
annual_savings = monthly_savings * 12
projected_savings = annual_savings + (annual_savings * 0.05)

print(f"Your monthly savings are ${fmt_number(monthly_savings)}.")
print(f"Projected savings after one year, with interest, is: ${fmt_number(projected_savings)}.")
