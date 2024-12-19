def floyds_triangle(n):
    num = 1  # Start from 1
    for i in range(1, n + 1):  # Loop for each row
        for j in range((n-i)*2):
            print(" ",end = " ")
        for j in range(1, i + 1):  # Loop for each number in a row
            print(num, end=" ")  # Print the number without newline
            num += 1  # Increment the number
        print()  # Newline after each row

# Example usage:
n = 5  # Number of rows
floyds_triangle(n)
