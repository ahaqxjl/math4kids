# 2位数加1位数进位加法
from random import randint, choice


def generate_tens():
    return randint(1, 9) * 10


def generate_sign():
    return choice(['+', '-'])


def generate_expression():
    a = generate_tens()
    b = generate_tens()

    sign = generate_sign()

    if sign == '+':
        ans = a + b
    elif sign == '-':
        ans = a - b
    else:
        return None

    if ans > 100 or ans < 0:
        return None
    else:
        return f'{a}{sign}{b}='


if __name__ == '__main__':
    for i in range(40):
        while True:
            exp = generate_expression()
            if exp:
                print(exp)
                break
