def count_digits(n):
    count = 0
    if n == 0:
        return 1
    if n < 0:
        n = -n  # Make it positive
    while n > 0:
        n = n // 10
        count += 1
    return count

# Input from user
try:
    num = int(input("Enter an integer: "))
    result = count_digits(num)
    print("Number of digits:", result)
except:
    print("Invalid input! Please enter an integer.")

