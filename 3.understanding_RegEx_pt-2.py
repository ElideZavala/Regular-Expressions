# --------------------------------------------------------------
# ------**## Understanding Regular Expressions Part 2 ##**------

import re

# ----------------------------------------------------------------
# *-*-*-*-*-*-* Example 4 ->>>> Caret
# match_result = re.finditer("^a", "a") # va a encontrar la a al principio de la cadena
# match_result = re.finditer("^a", "abc") # va a encontrar la a al principio de la cadena
# match_result = re.finditer("^a", "bac") # no va a encontrar la a al principio de la cadena

# match_result = re.finditer("^ab", "abc") # va a encontrar la ab al principio de la cadena

# match_result = re.finditer("^ab", "acb") # no va a encontrar la ab al principio de la cadena

# for match in match_result:
#     print(match)


# *-*-*-*-*-*-* Example 5 ->>>> Dollar
# Este va a determinar si una cadena termina con un caracter especifico
# match_result = re.finditer("a$", "a") # va a encontrar la a al final de la cadena
# match_result = re.finditer("a$", "formula") # <re.Match object; span=(6, 7), match='a'>
# match_result = re.finditer("a$", "cab") # no va a encontrar la a al final de la cadena


# for match in match_result:
#     print(match)

# *-*-*-*-*-*-* Example 6 ->>>> Star
# El * va a determinar si el caracter anterior aparece 0 o mas veces
match_result = re.finditer("ma*n", "mn") # va a encontrar la mn
match_result = re.finditer("ma*n", "man") # Puede terminar en 0 o mas n 
match_result = re.finditer("ma*n", "maaaaan") # <re.Match object; span=(0, 7), match='maaaaan'>
match_result = re.finditer("ma*n", "main") 
match_result = re.finditer("ma*n", "woman") # <re.Match object; span=(2, 5), match

for match in match_result:
    print(match)

