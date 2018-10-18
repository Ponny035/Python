# CSC233
# Given: 11 October 2018
#
#
# 1) Write a regular expression code in Python to handle the following
# six possible telephone number formats.
#
# xxx.xxx.xxxx
# xxx-xxx-xxxx
# xxx-xxxxxxx
# xxx xxx xxxx
# (xxx) xxx-xxxx
# (xxx) xxx xxxx
#
# E.g.,
#
# 428.515.5355 [0-9]{3}\.[0-9]{3}\.[0-9]{4}
# 086-315-5354 [0-9]{3}-[0-9]{3}-[0-9]{4}
# 428-5165455 [0-9]{3}-[0-9]{7}
# 350 535 5325 [0-9]{3} [0-9]{3} [0-9]{4}
# (089) 815-5395 \([0-9]{3}\) [0-9]{3}-[0-9]{4}
# (289) 888 5412 \([0-9]{3}\) [0-9]{3} [0-9]{4}

import re

def is_empty(any_structure):
    if any_structure:
        return False
    else:
        return True

Tel = "(?:[0-9]{3}\.[0-9]{3}\.[0-9]{4}|[0-9]{3}-[0-9]{3}-[0-9]{4}|[0-9]{3}-[0-9]{7})|[0-9]{3} [0-9]{3} [0-9]{4}|\([0-9]{3}\) [0-9]{3}-[0-9]{4}|\([0-9]{3}\) [0-9]{3} [0-9]{4}"
tel = re.compile(Tel)
input = raw_input("Input you phone Number: ")
find = tel.findall(input)
empty = is_empty(find)
if not empty:
    print(find +" is macth the pattern")
else:
    print("Input missmatch")

# Any other format would result in an error!
#
#
# 2) Write a regular expression code in Python to handle real numbers like:
# 12, 8., .12, 0.4, 12.5, 12.5E4, 12.5e4, 12.4E+4, 22E4, 13e-4, etc.
# Check Python and use only those supported in the language.
# For instance, 3e+5 is ok, but 3e+5. is not.
#
# num -> digit+ ( .digit+ )? ( E(+|-)? digit+)?
# digit -> 0 | 1 | ... | 9

Sci = "(?:[0-9]+(\.)*|\.)([0-9])*E*(?:\+([0-9])*|\-([0-9])*)*"
sci = re.compile(Sci)
input = raw_input("Input your number :")
find = sci.findall(input)
empty = is_empty(find)
if not empty:
    print(find +" is macth the pattern")
else:
    print("Input missmatch")
