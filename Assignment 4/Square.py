# Write a program in Python to find the square of any number using the function.
def square(n):
    s=n*n
    return s
a = int(input("Enter a number : "))
print(f"Square of {a} is :",square(a))