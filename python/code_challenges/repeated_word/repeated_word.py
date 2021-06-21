import re

def repeated_word(para:str):
    pattern = re.findall(r"[A-z]*\w", para)
    unilst = []
    for i in pattern:
        if i.lower() in unilst:
            return i
        else:
            unilst.append(i.lower())
