# 20以内加减法
from random import randint, choice

def generate_under20():
    return randint(1, 20)

def generate_sign():
    return choice(['+', '-'])


def generate_expression():
    a = generate_under20()
    b = generate_under20()

    sign = generate_sign()

    if sign == '+':
        ans = a + b
    elif sign == '-':
        ans = a - b
    else:
        return None

    if ans > 20 or ans < 0:
        return None
    else:
        return f'{a:>2}{sign}{b:<2}='


if __name__ == '__main__':
    for i in range(40):
        while True:
            exp = generate_expression()
            if exp:
                print(exp)
                break