# Input a five-digit number
number = input("Enter a five-digit number: ")

# Initialize an empty string to store the new number
new_number = ""

# Loop through each digit in the input number
for digit in number:
    # Add one to the digit and append it to the new_number string
    new_digit = str((int(digit) + 1) % 10)  # Use modulus to handle case when digit is 9
    new_number += new_digit

# Display the new number
print(f"The new number is: {new_number}")
