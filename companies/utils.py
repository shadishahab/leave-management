from random import seed, random

def random_code_generator(n):
    seed(1)
    values_list = []
    for _ in range(n):
        value = int(100000 + (random() * 90000))
        values_list.append(value)
    return values_list