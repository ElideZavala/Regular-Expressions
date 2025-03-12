# -------------------------------------------------------------------
# ----------------**## Special Sequences Part 1 ##**-----------------

import re

# -------------------------------------------------------------------
# *-*-*-*-*-*-*-*-*-* Example 22 ->>> \d - [0-9] *-*-*-*-*-*-*-*-*-*-
# \d atrapara cualquier digito (0-9)
# match_result = re.finditer(r"\d", "12 3.4 5 67.8 90")

# for match in match_result:
#     print(match)  

# Output:
#<re.Match object; span=(0, 1), match='1'>
#<re.Match object; span=(1, 2), match='2'>
#<re.Match object; span=(3, 4), match='3'>
#<re.Match object; span=(5, 6), match='4'>
#<re.Match object; span=(7, 8), match='5'>
#<re.Match object; span=(9, 10), match='6'>
#<re.Match object; span=(10, 11), match='7'>
#<re.Match object; span=(12, 13), match='8'>
#<re.Match object; span=(14, 15), match='9'>
#<re.Match object; span=(15, 16), match='0'>
# -------------------------------------------------------------------
# *-*-*-*-*-*-*-*-*-* Example 23 ->>> \D - [a-zA-Z_ ] + symbols *-*-*-*-*-*-*-*-*-*-
# \D atrapara cualquier cosa que no sea un digito (0-9)
match_result = re.finditer(r"\D", "12 45 # HI There < ? _")

for match in match_result:
    print(match)

# Output:
# <re.Match object; span=(2, 3), match=' '>
# <re.Match object; span=(5, 6), match=' '>
# <re.Match object; span=(6, 7), match='#'>
# <re.Match object; span=(7, 8), match=' '>
# <re.Match object; span=(8, 9), match='H'>
# <re.Match object; span=(9, 10), match='I'>
# <re.Match object; span=(10, 11), match=' '>
# <re.Match object; span=(11, 12), match='T'>
# <re.Match object; span=(12, 13), match='h'>
# <re.Match object; span=(13, 14), match='e'>
# <re.Match object; span=(14, 15), match='r'>
# <re.Match object; span=(15, 16), match='e'>
# <re.Match object; span=(16, 17), match=' '>
# <re.Match object; span=(17, 18), match='<'>
# <re.Match object; span=(18, 19), match=' '>
# <re.Match object; span=(19, 20), match='?'>
# <re.Match object; span=(20, 21), match=' '>
# <re.Match object; span=(21, 22), match='_'>
 
# -------------------------------------------------------------------
# *-*-*-*-*-*-*-*-*-* Example 24 ->>> \s - [space, tab, " ", "\t", "\n"] *-*-*-*-*-*-*-*-*-*-
# \s atrapara cualquier espacio en blanco, tabulacion, salto de linea, etc.

# -------------------------------------------------------------------
# *-*-*-*-*-*-*-*-*-* Example 25 ->>> \S - [a-zA-Z0-9_] *-*-*-*-*-*-*-*-*-*-
# \S atrapara cualquier cosa que no sea un espacio en blanco, tabulacion, salto de linea, etc.
