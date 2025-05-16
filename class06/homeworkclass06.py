import re

text = "Please contact us at support@example.com or sales@company.org. You can also reach out to admin123@school.edu."

pattern = r"\b[\w.-]+@[\w.-]+\.\w+\b"

emails = re.findall(pattern, text)

print("Extracted emails:", emails)