# --------------------------------------------------------------------
# --------------------**## The Raw String ##**------------------------

import re

# ----------------------------------------------------------------------
# *-*-*-*-*-*-*-*-* Example 21 ->>>> r - raw string *-*-*-*-*-*-*-*-*-*-

# \t es equivalente a un tabulador
# r ayuda a que el string sea interpretado como un string crudo
# sin importar los caracteres especiales que tenga

pattern = "\tBook"
pattern = r"\tBook"
pattern = r"\d"
print(pattern)  