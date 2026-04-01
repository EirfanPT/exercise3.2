try:
    num = float(input("Enter a number: "))
    print("Square of the number is:", num ** 2)
except ValueError:
    print("Invalid input! Please enter a number.")