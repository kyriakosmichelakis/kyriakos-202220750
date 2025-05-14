def invert_dict(d):
    return {value: key for key, value in d.items()}

original = {"a": 1, "b": 2, "c": 3}
inverted = invert_dict(original)
print(inverted)