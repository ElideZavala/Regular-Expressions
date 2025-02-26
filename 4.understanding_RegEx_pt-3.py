# ----------------------------------------------------------------
# ------ **## Understanding Regular Expressions Part 3 ##** ------

import re

# ----------------------------------------------------------------
# *-*-*-*-*-*-* Example 7 ->>>> Plus
# El + va a determinar si el caracter anterior aparece 1 o mas veces
# la diferencia con el * es que el * puede ser 0 veces y el + no puede ser 0 veces
# no hay limite de cuantas veces puede aparecer el caracter anterior

# match_result = re.finditer("ma+n", "mn") # no va a encontrar la mn
# match_result = re.finditer("ma+n", "man") # <re.Match object; span=(0, 3), match='man'>
# match_result = re.finditer("ma+n", "maaaaan") # <re.Match object; span=(0, 7), match='maaaaan'>

# for match in match_result:
#     print(match)


# *-*-*-*-*-*-* Example 8 ->>>> Question Mark
# El ? va a determinar si el caracter anterior aparece 0 o 1 vez
# solo busca si el caracter anterior aparece 0 o 1 vez

# match_result = re.finditer("ma?n", "mn") 
# match_result = re.finditer("ma?n", "man") 
# match_result = re.finditer("ma?n", "maaan") # ya que el caracter anterior es a, no va a encontrar la cadena
# match_result = re.finditer("ma?n", "woman") # <re.Match object; span=(2, 5), solo aparece una vez

# for match in match_result:
#     print(match)



# *-*-*-*-*-*-* Example 9 ->>>> Curly Brackets
# Los {} va a determinar si el caracter anterior aparece un numero especifico de veces

# match_result = re.finditer("a{2,4}", "abc dat") # buscara la cadena que tenga 2 a 4 veces la letra a

# # solo detectara de 2 a 4 veces la letra a
# match_result = re.finditer("a{2,4}", "abc daat")  # <re.Match object; span=(5, 7), match='aa'>

# match_result = re.finditer("a{2,4}", "aabc daaat")  
# # <re.Match object; span=(0, 2), match='aa'>
# # <re.Match object; span=(6, 9), match='aaa'>

# match_result = re.finditer("a{2,4}", "aabc daaat caaaat")  
# """
# <re.Match object; span=(0, 2), match='aa'>
# <re.Match object; span=(6, 9), match='aaa'>
# <re.Match object; span=(12, 16), match='aaaa'>
# """

# match_result = re.finditer("a{2,4}", "aabc daaat caaaat daaaaat")  
# """
# <re.Match object; span=(0, 2), match='aa'>
# <re.Match object; span=(6, 9), match='aaa'>
# <re.Match object; span=(12, 16), match='aaaa'>
# <re.Match object; span=(19, 23), match='aaaa'>
# """

# for match in match_result:
#     print(match)


# *-*-*-*-*-*-* Example 10 ->>>> {} - Braces

match_result = re.finditer("[0-9]{2,4}", "abc 123 def ghi 45") # buscara que la cadena tenga de 2 a 4 digitos seguidos del 0 al 9
match_result = re.finditer("[0-9]{2,4}", "12 345 60789 12398 455") # <re.Match object; span=(4, 8), match='1234'>


for match in match_result:
    print(match)
