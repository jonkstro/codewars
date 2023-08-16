def open_or_senior(data):
    lista = []
    for i in data:
        age = i[0]
        handicap = i[1]
        if age >= 55 and handicap > 7:
            lista.append('Senior')
        else:
            lista.append('Open')
        # print(age, handicap)
        # print(lista)
        
    return lista

open_or_senior([(45, 12),(55,21),(19, -2),(104, 20)])