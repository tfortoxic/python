def main(text):
    keyword = "#"
    for x in text.split(" "):
        if len(x) == 5:
            keyword = x
            break

    print("This is the word of length 5:", x)
    
    text_for_encoding = text.replace(" ", "")
    repeat_count_for_keyword = len(text_for_encoding) // len(keyword)
    keyword_for_encoding = keyword * (repeat_count_for_keyword + 1)
    print("This is the keyword repeat count:", repeat_count_for_keyword)

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    int_to_char = {a + 1: b for a, b in enumerate(alphabet)}
    char_to_int = {b: a + 1 for a, b in enumerate(alphabet)}
    
    encoded_text = []

    for i in range(len(text_for_encoding)):
        text_char = text_for_encoding[i]
        key_char = keyword_for_encoding[i]
        
        if text_char in char_to_int and key_char in char_to_int:
            encoded_int = char_to_int[text_char] + char_to_int[key_char]
            if encoded_int > 26:
                encoded_int -= 26
            encoded_char = int_to_char[encoded_int]
            encoded_text.append(encoded_char)
        else:
            encoded_text.append(text_char)
    
    print("".join(encoded_text))

main("i am shree krishna paudel")
