# Write a program in Python to check if a given number is even or odd using the function.
def odd(num):
    if num%2==0:
        print(f"{num} is even number")
    else:
     print(f"{num} is odd number")
n= int (input("Enter a number to check ODD or EVEN : ",))
odd(n)