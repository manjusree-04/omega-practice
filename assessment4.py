def sum_of_evens(n):
    total = 0
    for i in range(2, n + 1, 2):  # Start from 2 and go up to n, stepping by 2 (to only consider even numbers)
        total += i
    return total

# Input: a positive integer n
n = int(input("Enter a positive integer n: "))

# Calculate and print the sum of even numbers
result = sum_of_evens(n)
print(f"The sum of all even numbers between 1 and {n} is: {result}")
