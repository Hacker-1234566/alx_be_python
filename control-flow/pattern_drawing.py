# pattern_drawing.py

# Prompt the user for the pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# While loop for rows
while row < size:
    # For loop for columns
    for col in range(size):
        print("*", end="")
    print()  # Move to next line after finishing a row
    row += 1

