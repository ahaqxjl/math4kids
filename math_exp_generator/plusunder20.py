# 10以内加法
from random import randint, choice

def generate_under20():
    return randint(1, 19)


def generate_expression():
    a = generate_under20()
    b = generate_under20()

    ans = a + b
    if ans > 20:
        return None
    else:
        return f'{a:>2}+{b:>2}='


if __name__ == '__main__':
    for i in range(40):
        while True:
            exp = generate_expression()
            if exp:
                print(exp)
                break