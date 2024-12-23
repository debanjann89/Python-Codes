
        # Input: Prompt the user for a decimal number
decimal_number = int(input("Enter a decimal number: "))
original_number = decimal_number  # Store the original number for reference

        # Handle the edge case where the input is 0
if decimal_number == 0:
    print("The octal equivalent of 0 is 0")


        # Process: Convert the decimal number to octal using a loop
octal_number = ""
while decimal_number > 0:
        remainder = decimal_number % 8
        octal_number = str(remainder) + octal_number
        decimal_number //= 8

        # Output: Display the octal equivalent
print(f"The octal equivalent of {original_number} is {octal_number}")


