# --------------------------------------------------------------------
# ---------- **## Regular Expressions Methods Part 1 ##** ------------

import re

# --------------------------------------------------------------------
# *-*-*-*-*-*- Example 14 ->>>> Findall() Method -*-*-*-*-*-*-*-*-*-*-
# --------------------------------------------------------------------
# The findall() method returns a list containing all matches.

# Syntax: re.findall(pattern, string, flags=0)

# string = "hello 12 hi 65 123 howdy 784 907"
# pattern = '\d+' # '\d' ->> Matches any digit character (0-9). Equivalent to [0-9].

# result = re.findall(pattern, string)
# print( result ) # Output: ['12', '65', '123', '784', '907']



# *-*-*-*-*-*- Example 15 ->>>> Split() Method -*-*-*-*-*-*-*-*-*-*-
# --------------------------------------------------------------------
# The split() method returns a list where the string has been split at each match.
# Si el patron coincide con el string, el string se divide en cada coincidencia.

# Syntax: re.split(pattern, string, maxsplit=0, flags=0)
# string = "hello 12 hi 65 123 howdy 784 907"
# pattern = "\d+" # Todos los digitos del 0 al 9

# result = re.split(pattern, string)

# print( result ) # Output: ['hello ', ' hi ', ' ', ' howdy ', ' ', '']
# # quitar los espacios en blanco y las ', ' y unir 
# result = ''.join(result)
# print( result ) # Output: hello hi howdy

# string = "hello there"
# pattern = "\d+" 

# result = re.split(pattern, string)
# print( result ) # Output: ['hello there'] # No hay coincidencias, por lo tanto no se divide el string.
# *-*-*-*-*-*- Example 16 ->>>> Sub() Method -*-*-*-*-*-*-*-*-*-*-
# --------------------------------------------------------------------
# The sub() method replaces the matches with the text of your choice.

# Syntax: re.sub(pattern, repl, string, count=0, flags=0)
# string = "abc 12\
#     de 23 \n f45 621" # el \ es para continuar en la siguiente linea

 # \n ->> New line, \t ->> Tab, \b ->> Backspace, \r ->> Carriage return

# print(string)

# \s ->> Matches any whitespace character (spaces, tabs, line breaks).
# \s+ ->> Matches any whitespace character (spaces, tabs, line breaks) one or more times.  

# pattern = "\s+"   

# No se elimina el \n, solo los espacios en blanco

# print(re.findall(pattern, string))

# replace = "" # Reemplazar los espacios en blanco por nada

# new_string = re.sub(pattern, replace, string) 
# print(new_string) # Output: abc12de23f45621

# *-*-*-*-*-*- Example 17 ->>>> Sub() Method -*-*-*-*-*-*-*-*-*-*-
# --------------------------------------------------------------------
# The subn() method is similar to sub() but returns a tuple containing the new string value and the number of replacements.

# Syntax: re.subn(pattern, repl, string, count=0, flags=0)


string ="abc 12\
    de 23 \n f45 621"

pattern = "\s+"
replace = ""

# Reemplazar solo el primer espacio en blanco
new_string = re.sub(pattern, replace, string, 1) # Output: abc12de 23 \n f45 621
# Remplazar varios espacios en blanco
new_string = re.sub(pattern, replace, new_string, 2) # Output: abc12de23 f45 621
# new_string = re.sub(pattern, replace, new_string, 3) # Output: abc12de23f45 621 
new_string = re.sub(pattern, replace, new_string, 4) # Output: abc12de23f45621

print(new_string) 
