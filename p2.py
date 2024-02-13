strings = ["apple", "banana", "orange","grape","peach"]

sorted_strings = sorted(strings, key=lambda s: (len(s), s))
print(strings)