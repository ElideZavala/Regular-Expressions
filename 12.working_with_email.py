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
    pattern = r"[a-zA-Z0-9]+@" # obtenenis los valores que coincidan             
    pattern = r"[a-zA-Z0-9-_]+@"   # obtenemos       
    pattern = r"[a-zA-Z0-9-_\.]+@"  
    pattern = r"[a-zA-Z0-9-_\.]+@[a-zA-Z-]+" # Obtenemos 
    # pattern = r"[a-zA-Z0-9-_\.]+@[a-zA-Z-]+\."
    # pattern = r"[a-zA-Z0-9-_\.]+@[a-zA-Z-]+\.com"
    pattern = r"[a-zA-Z0-9-_\.]+@[a-zA-Z-_]+\.(com|edu|io)+"
    pattern = r"[a-zA-Z0-9-_\.]+@[a-zA-Z-_]+\.[a-z]+"
    pattern = r"([a-zA-Z0-9-_\.]+)@([a-zA-Z-_]+)\.([a-z]+)" 


    matches_result = re.finditer(pattern, emails) 

    for match in matches_result:
        # print(match)    
        # print(match.group()) # obtenemos el valor que coincida
        # print(match.group(1)) # Obtenemos el valor que coincida en el primer grupo
        print(match.group(1,2,3)) # obtenemos el valor que coincida con cada grupo
        # print(match.span()) # obtenemos la posicion de la coincidencia   