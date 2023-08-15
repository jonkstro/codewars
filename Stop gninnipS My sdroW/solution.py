def spin_words(sentence):
    lista = sentence.split()
    for i in range(len(lista)):
        if len(lista[i]) >= 5:
            lista[i] = lista[i][::-1]
    return (" ".join(lista))
