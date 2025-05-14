a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Union: all unique elements from both sets
union = a | b
print("Union:", union)

# Intersection: elements common to both sets
intersection = a & b
print("Intersection:", intersection)

# Difference: elements in a but not in b
difference = a - b
print("Difference (a - b):", difference)

# Symmetric Difference: elements in either a or b, but not both
symmetric_difference = a ^ b
print("Symmetric Difference:", symmetric_difference)