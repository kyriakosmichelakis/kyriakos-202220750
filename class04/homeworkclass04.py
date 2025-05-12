# Get 5 valid numbers from the user
numbers = []
 
for i in range(5):
    while True:
        try:
            num = float(input(f"Enter number {i + 1}: "))
            numbers.append(num)
            break  # Exit the loop if input is valid
        except ValueError:
            print("Invalid input. Please enter a number.")
 
# Show original list
print("Original list:", numbers)
 
# Sort and show the sorted list
numbers.sort()
print("Sorted list:", numbers)
 
# Remove the largest number (last item) and show the updated list
numbers.pop()
print("List after removing largest number:", numbers)
 
# Calculate and show average
average = sum(numbers) / len(numbers)
print("Average of remaining numbers:", average)