# -----------------------------------------------------------------
#! ------ **## Understanding Regular Expressions Part 1 ##** ------

import re 

# ----------------------------------------------------------------
# *-*-*-*-*-*-* Example 2 ->>>> [] Square brackets
# match_result = re.finditer("[abc]", "a") 
# # match_result = re.finditer("[abc]", "ac")
# match_result = re.finditer("[abc]", "hey there")
# match_result = re.finditer("[abc]", "abc de ca")
# match_result = re.finditer("[a-e]", "abc de ca cat dog elephant")
# match_result = re.finditer("[^a-e]", "abc de ca cat dog elephant")
# match_result = re.finditer("[^0-5]", "12 34 56 78 90 23 22 11 68 90")

# for match in match_result:
#     print(match)


# ----------------------------------------------------------------
# *-*-*-*-*-*-* Example 3 ->>>> [^] Period
match_result = re.finditer(".", "123") # va a encontrar cualquier caracter en la cadena
match_result = re.finditer(".", "abc")
match_result = re.finditer("..", "abc")
match_result = re.finditer("..", "abcd") # va a encontrar cualquier caracter en la cadena de 2 en 2


for match in match_result:
    print(match) 
