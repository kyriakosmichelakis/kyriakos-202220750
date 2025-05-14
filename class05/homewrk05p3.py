prime_numbers = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31}

# Ask the user for a number
try:
    num = int(input("Enter a number: "))

    # Check if it's in the set of prime numbers
    if num in prime_numbers:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is NOT in the prime number set.")
except ValueError:
    print("Invalid input. Please enter a whole number.")