def row_sum_odd_numbers(n):
    soma = 0
    for i in range(n):
        if i % 2 != 0:
            soma += i
            print (soma)
    return soma

row_sum_odd_numbers(13)