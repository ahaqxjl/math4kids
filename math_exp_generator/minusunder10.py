# 10以内加法
from random import randint, choice

def generate_under10():
    return randint(1, 9)


def generate_expression():
    a = generate_under10()
    b = generate_under10()

    ans = a - b
    if ans < 0:
        return None
    else:
        return f'{a}-{b}='


if __name__ == '__main__':
    for i in range(40):
        while True:
            exp = generate_expression()
            if exp:
                print(exp)
                break