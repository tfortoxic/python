# Example: Joining a list of strings into a single string
words = ["Hello", "world", "this", "is", "Python"]
sentence = " ".join(words)
print(sentence)

# Example: Joining a list of strings with a different separator
items = ["apple", "banana", "cherry"]
result = ", ".join(items)
print(result)

# Example: Joining a list of numbers into a single string
numbers = [1, 2, 3, 4, 5]
result = "-".join(map(str, numbers))
print(result)

# Example: Joining a list of lines to form a paragraph
lines = [
    "This is the first line.",
    "This is the second line.",
    "This is the third line."
]
paragraph = "\n".join(lines)
print(paragraph)

# Example: Joining nested lists into a single string
nested_list = [["Join", "us"], ["for", "Python"], ["lessons"]]
result = " ".join([" ".join(inner_list) for inner_list in nested_list])
print(result)
