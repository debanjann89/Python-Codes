# Input a five-digit number
number = int(input("Enter a five-digit number: "))

# Initialize the reversed number
reversed_number = 0

# Reverse the number using a loop
while number > 0:
    digit = number % 10               # Extract the last digit
    reversed_number = reversed_number * 10 + digit  # Build the reversed number
    number = number // 10             # Remove the last digit

# Display the reversed number
print(f"The reversed number is: {reversed_number}")
