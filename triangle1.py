# Input the time taken by the worker to complete the job
time_taken = float(input("Enter the time taken by the worker (in hours): "))

# Determine the worker's efficiency based on the time taken
if 2 <= time_taken < 3:
    print("The worker is Highly Efficient.")
elif 3 <= time_taken < 4:
    print("The worker is ordered to improve speed.")
elif 4 <= time_taken < 5:
    print("The worker is given training to improve speed.")
elif time_taken >= 5:
    print("The worker has to leave the company.")
else:
    print("Invalid input. Time taken cannot be less than 2 hours.")
