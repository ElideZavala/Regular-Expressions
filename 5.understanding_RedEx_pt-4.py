# ------------------------------------------------------------------------------
# -------**## Understanding Regular Expressions in Python - Part 4 ##**---------

import re
# match_result = re.finditer()

# ------------------------------------------------------------------------------
# *-*-*-*-*-*-* Example 11 ->> | - Alternation 
 # El | se utiliza para hacer coincidir cualquiera de las expresiones separadas por él.

# match_result = re.finditer("a|b", "abcde") # a or b
# match_result = re.finditer("z|c", "abcde") # z or c
# match_result = re.finditer("a|b|c", "abcde") # a or b or c
# match_result = re.finditer("z|c", "zzc") # z or c

# for match in match_result:
#     print(match) 

# *-*-*-*-*-*-* Example 12 ->> () Group
# Los paréntesis se utilizan para agrupar expresiones.

# match_result = re.finditer("(a|b|c)xz", "axz bxz cxz") # a or b or c, x, z en ese orden
# match_result = re.finditer("(a|b|c)xz", "abc xz") # no hay coincidencia
# match_result = re.finditer("(a|b|c)xz", "cxz") # c, x, z en ese orden
# match_result = re.finditer("(a|b|c)xz", "abxz") # a, b, x, z en ese orden
# match_result = re.finditer("(a|b|c)xz", "abcxz") # a, b, x, z en ese orden


# for match in match_result:
#     print(match)


# *-*-*-*-*-*-* Example 13 ->> \ Backslash 
# Se utiliza para escapar de caracteres especiales.

match_result = re.match("\^xz", "^xz") # ^, x, z en ese orden
print(match_result)

















