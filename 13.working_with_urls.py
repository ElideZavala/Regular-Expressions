# ----------------------------------------------------------------------------------------------------
# -----------------------------------**## Working with URLs ## ** ------------------------------------
# 

import  re

with open('urls.txt') as file:
    urls = file.read()

    pattern = r"https://([a-zA-Z]+)\."
    pattern = r"https?://([a-zA-Z]+)\." # Es signo ? es cuando un valor es opcional.
    pattern = r"https?://([a-zA-Z]+)\.([a-zA-Z0-9-]+)" 
    pattern = r"https?://(www\.)?([a-zA-Z]+)\.([a-zA-Z0-9-]+)" # El grupo www podria ser opcional.

    matches_result = re.finditer(pattern, urls)

    for match in matches_result:
        print(match)