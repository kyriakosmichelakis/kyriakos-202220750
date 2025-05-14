# Create a dictionary of students and their grades
students = {
    "Kyriakos": [85, 90, 78],
    "Kirk": [70, 88, 92],
    "Michel": [95, 100, 98]
}

# Add a new student
students["Michelakis"] = [80, 84, 89]

# Update grades for an existing student
students["Kyriakos"].append(95)

# Calculate and print the average grade for each student
for name, grades in students.items():
    average = sum(grades) / len(grades)
    print(f"{name}'s average grade: {average:.2f}")