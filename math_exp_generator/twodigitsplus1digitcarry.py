# 2位数加1位数进位加法
from random import randint, choice

def generate_2digits():
    return randint(10, 99)


def generate_1digit():
    return randint(1, 9)


def generate_expression():
    a = generate_2digits()
    b = generate_1digit()
    if a + b >= 100:
        return None
    elif a % 10 + b < 10:
        return None
    else:
        exp = choice([f'{a}+{b:>2}=', f'{b:>2}+{a}='])
        return exp


if __name__ == '__main__':
    for i in range(40):
        while True:
            exp = generate_expression()
            if exp:
                print(exp)
                break
