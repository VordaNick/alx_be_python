while True:
    n = int(input("Enter the size of the pattern: "))
    if n > 0:
        break
    else:
        print("Invalid input. Please enter a positive integer.")
for i in range(n):
    print("*" * n)