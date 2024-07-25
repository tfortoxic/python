'''A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence
"The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).
Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.'''

str = "The quick brown fox jumps over the lazy dog"
seen_character = set()
for item in str.lower():
    if item.isalpha() and item not in seen_character:
        seen_character.update(item)


if len(seen_character)== 26:
    print("it is a pangram")

else:
    print("it is not a pangram")
print(len(seen_character))