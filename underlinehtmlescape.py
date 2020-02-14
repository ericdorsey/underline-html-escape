#!/usr/bin/env python3

"""
Given input raw string (even with backslash escaped double quotes), output
new string with every character in the string prepended with the &#818;
HTML escape code "combining low line", which more or less ends up looking
like underlined text.
"""

# A raw string cannot end in backslash, so leave
# a space at the end instead, i.e.:
# my_str = r""""You need a 2\"x3\" """
my_str = r""""You need a 2\"x3\" """

my_str = my_str.split(" ")
print(my_str)

# &#818; is the "combining low line" (underscore)
my_prepend = "&#818;"
new_out = []

for i, v in enumerate(my_str):
    print(i, v)
    temp_string = ""
    for j in v:
        print(j)
        j = my_prepend + j
        if j.endswith("\\"):
            j += "\\"
        print(j)
        temp_string += j
    new_out.append(temp_string)

print()
new_out = f"{my_prepend} ".join(new_out)
new_out = new_out.rstrip(" ")
new_out = new_out.rstrip(my_prepend)
print(new_out)
