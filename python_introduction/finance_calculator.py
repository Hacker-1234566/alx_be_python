def fmt_number(x):
    """Format number: drop .0 for whole numbers, otherwise show up to 2 decimals."""
    x = float(x)
    if x.is_integer():
        return str(int(x))
    return f"{x:.2f}".rstrip('0').rstrip('.')

# Prompt the user exactly as required
income = float(input("Enter your monthly income: "))
expenses = float(input("Enter your total monthly expenses: "))

# Calculations
monthly_savings = income - expenses
annual_savings = monthly_savings * 12
projected_savings = annual_savings * 1.05  # 5% interest

# Output with exact wording and punctuation
print(f"Your monthly savings are ${fmt_number(monthly_savings)}.")
print(f"Projected savings after one year, with interest, is: ${fmt_number(projected_savings)}.")
