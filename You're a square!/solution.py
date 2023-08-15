import math


def is_square(n):
    # if n == 0: return True
    if n >=0 and math.sqrt(n) % 1 == 0:
        return True
    # for i in range(n):
    #     if i ** 2 == n:
    #         return True
    return False