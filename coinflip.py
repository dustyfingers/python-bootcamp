import random


def coin_flip():
    result = random.randint(0, 1)
    if result:
        return 'heads'
    else:
        return 'tails'


print(coin_flip())
print(coin_flip())
print(coin_flip())
print(coin_flip())
