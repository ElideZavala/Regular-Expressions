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
# \b

# string = "possibleim 12 54 # . hi possible \n There possible \t < ? _ > %  ^ impossible"

# Buscara por la palabra possible que se encuentre al inicio de la cadena
# match_result = re.finditer(r"\bpossible", string)
# \b se utiliza para buscar la palabra que se encuentre al inicio de la cadena


# # *-*-*-*-* Case 2 - At the end *-*-*-*-*
# string = "possibleim 12 54 # . hi possible \n There possible \t < ? _ > %  ^ impossible"

# match_result = re.finditer(r"\Bpossible", string)
# # \b se utiliza para buscar la palabra que se encuentre al final de la cadena

# for match in match_result:
#     print(match)

# *-*-*-*-*-*-*-*-*-* Example 29->>> \B *

# *-*-*-*-* Case 1 - Not at the begginning  *-*-*-*-*

# string = "heater 12 54 # . hi \n There  \t < ? _ > %  ^ unheated noheat"

# match_result = re.finditer(r"\Bheat", string)
# # \B se utiliza para buscar la palabra que no se encuentre al inicio de la cadena
# # aqui se obtiene las palabras, unheated y noheat 

# for match in match_result:
#     print(match)



# *-*-*-*-* Case 2 - Not at the end  *-*-*-*-*

string = "heater 12 54 # . hi \n There  \t < ? _ > %  ^ unheated noheat"

match_result = re.finditer(r"heat\B", string)
# \B se utiliza para buscar la palabra que no se encuentre al final de la cadena
# aqui se obtiene las palabras, heater y unheated, es decir empesara con la h, que heat no se ecuentre al final de la cadena

for match in match_result:
    print(match)

'''
<re.Match object; span=(0, 4), match='heat'>
<re.Match object; span=(46, 50), match='heat'>
'''








