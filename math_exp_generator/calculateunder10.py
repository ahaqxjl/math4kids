# 20以内加减法
from random import randint, choice

def generate_under10():
    return randint(1, 9)

def generate_sign():
    return choice(['+', '-'])


def generate_expression():
    a = generate_under10()
    b = generate_under10()

    sign = generate_sign()

    if sign == '+':
        ans = a + b
    elif sign == '-':
        ans = a - b
    else:
        return None

    if ans > 10 or ans < 0:
        return None
    else:
        return f'{a}{sign}{b}='


if __name__ == '__main__':
    for i in range(40):
        while True:
            exp = generate_expression(answer=True)
            if exp:
                print(exp)
                break