# --------------------------------------------------------------------------------
# -------------------------** Working with Emails **------------------------------

import re

with open("emails.txt") as file:
    emails = file.read()

    # minusculas y mayusculas [a-zA-Z]    
    # numeros [0-9]
    # guion bajo _
    # guion -
    # El + es para que se repita una o mas veces
    pattern = r""
    pattern = r"[a-zA-Z0-9]+@"
    pattern = r"[a-zA-Z0-9-_]+@"
    pattern = r"[a-zA-Z0-9-_\.]+@"
    pattern = r"[a-zA-Z0-9-_\.]+@[a-zA-Z-]+"
    # pattern = r"[a-zA-Z0-9-_\.]+@[a-zA-Z-]+\."
    # pattern = r"[a-zA-Z0-9-_\.]+@[a-zA-Z-]+\.com"
    pattern = r"[a-zA-Z0-9-_\.]+@[a-zA-Z-_]+\.(com|edu|io)+"
    pattern = r"[a-zA-Z0-9-_\.]+@[a-zA-Z-_]+\.[a-z]+"

    matches_result = re.finditer(pattern, emails)

    for match in matches_result:
        print(match)