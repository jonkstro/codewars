import re

def to_camel_case(text):
    lista2 = []
    if text == "": return text
    lista = re.split(r'_|-', text)
    # print(" ".join(lista).upper()) 
    lista2.append(lista[0])
    for i in range(len(lista)):
        if i > 0:
            lista2.append(lista[i][0].upper()+lista[i][1:])
        # print("".join(lista2))
    print ("".join(lista2))
    return ("".join(lista2))

to_camel_case('The-Stealth-Warrior')