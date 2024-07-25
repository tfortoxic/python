'''You'll be given a list of two strings, and each will contain exactly one colon (":") in the middle (but not at beginning or end). The length of the strings, before and after the colon, are random.

Your job is to return a list of two strings (in the same order as the original list), but with the characters after each colon swapped.

Examples
["abc:123", "cde:456"]  -->  ["abc:456", "cde:123"]
["a:12345", "777:xyz"]  -->  ["a:xyz", "777:12345"]'''

def swaptail(original_list):
    split_list = [item.split(":") for item in original_list]#this would split thee list where : is

    swapped_list = [[parts[1], parts[0]] for parts in split_list]
    
    result_list = [":".join(parts) for parts in swapped_list]
    
    return result_list

original_list = ["abc:123", "cde:456"]
print("list before tailswap\n",original_list)
swapped_list = swaptail(original_list)
print("this is after swap",swapped_list)
