# -----------------------------------------------------------------------------------------
# ------------------------**## Special Sequences - Part 2 ##**-----------------------------

import re

# -----------------------------------------------------------------------------------------
# *-*-*-*-*-*-*-*-*-* Example 26->>> \w - [a-zA-Z0-9_] *

# match_result = re.finditer(r"\w", "12 54 # \n Theme < ? _")
# # con el uso de \w se obtiene todos los caracteres alfanumericos y el guion bajo
# # en este caso se obtiene los siguientes caracteres: 1, 2, 5, 4, T, h, e, m, e, _
# # no se obtiene los caracteres: espacio, numeral, salto de linea, menor que, signo de interrogacion

# for match in match_result:
#     print(match)

# *-*-*-*-*-*-*-*-*-* Example 27->>> \W - not [a-zA-Z0-9_] *

# match_result = re.finditer(r"\W", "12 54 # \n Theme < ? _")
# con el uso de \W se obtiene todos los caracteres que no son alfanumericos y el guion bajo
# en este caso se obtiene los siguientes caracteres: espacio, numeral, salto de linea, menor que, signo de interrogacion    
# no se obtiene los caracteres: 1, 2, 5, 4, T, h, e, m, e, _

# for match in match_result:
#     print(match)

# *-*-*-*-*-*-*-*-*-* Example 28->>> \b *

# *-*-*-*-* Case 1 - At the begginning of the string *-*-*-*-*
