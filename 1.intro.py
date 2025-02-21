# --------------------------------------------------------------------------
#! --- ** ## Introduction to Regular Expressions (RegEx) in Python ## ** ---

import re

# *-*-*-*-*-*-* Example 1 *
test_string = "Hat"
test_string = "cat"
test_string = "dog"
test_string = "era"

pattern = ".a." # cual quier caracter entre la a y la a

result = re.match(pattern, test_string)
print(result) # <re.Match object; span=(0, 3), match='cat'>