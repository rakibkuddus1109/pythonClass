# Regular Expression : Advance of strings

import re   # to import regular expression

# a="this is my mobile number 809 931-9336"

# Symbols
    # \d : digits
    # \w : alphanumeric
    # {} : length specification

format_str = r"\d{3} \d{3}-\d{4}"   # Start with "r" to denote as regular expression

# Operations that can be performed:
    # Match : performs match at starting of string only
    # Search : performs seach at any position in string but only for single entity
    # Findall : finds all matching items from string

# matching

# a="this is my mobile number 809 931-9336"
# a="809 931-9336 is my mobile number"

# matching1 = re.match(format_str,a)
# print(matching1)   # It can't find number from a for 1st example as it is not at beginning
# print(matching1.group())   # group() gets the value

# searching

# a="this is my mobile number 809 931-9336"

# searching1 = re.search(format_str,a)
# print(searching1)
# print(searching1.group())

# findall

# a="this is my mobile numbers 809 931-9336, 965 217-3210"

# findall1 = re.findall(format_str,a)
# print(findall1)