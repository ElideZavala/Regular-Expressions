# --------------------------------------------------------------
# ------------**## Regular Expression Methods ##**--------------

import re
# --------------------------------------------------------------
# # *-*-*-*-*-*-* Example 18 *-*-*-*-*-*-*- subn() *-*-*-*-*-*-*-
# # subn() method is similar to sub() method but it returns a tuple containing the new string value and the number of replacements.

# string ="abc 12 de 23 f45"
# pattern = "\s+"
# replace = ""

# new_string = re.subn(pattern, replace, string)
# print(new_string) # Output: ('abc12de23f45', 4) # 4 reemplazos

# *-*-*-*-*-*-* Example 19 *-*-*-*-*-*-*- search() *-*-*-*-*-*-*-

# search() method searches for the first occurrence of the pattern in the string.
# Syntax: re.search(pattern, string, flags=0)

# string = 'is fun python'
# pattern = "python" # \A ->> Matches if the specified characters are at the start of a string

# # La diferencia con match() es que search() busca en toda la cadena, no solo al principio.

# match_result1 = re.search(pattern, string)
# match_result2 = re.match(pattern, string)
# print(match_result1) # Output: <re.Match object; span=(0, 6), match='python'>
# print(match_result2) # Output: <re.Match object; span=(0, 6), match='python'>

# *-*-*-*-*-*-* Example 20 *-*-*-*-*-*-*- group() *-*-*-*-*-*-*-
string = "12345 67, 7894 1122"
pattern = "(\d{3}) (\d{2})" # \d ->> Hacer coincidir cualquier dígito (0-9), {3} ->> Hacer coincidir exactamente 3 veces, {2} ->> Hacer coincidir exactamente 2 veces

match = re.search(pattern, string)
print(match) # Output: <re.Match object; span=(6, 12), match='345 67'>

if match: 
    print(match.group()) # Output: 345 67

    print(match.start() ) # Output: 2
    print(match.end() ) # Output: 8
    print(match.span()) # Output: (2, 8)
else:
    print("Pattern not found")