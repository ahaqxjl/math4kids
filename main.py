import argparse
from math_exp_generator.twodigitsplus1digitcarry import generate_expression


def get_args_parser():
    parser = argparse.ArgumentParser('一年级数学出题神器')
    parser.add_argument('-n', '--num_expressions', default=40, type=int, help='数学题目数量')
    return parser


if __name__ == '__main__':
    parser = get_args_parser()
    args = parser.parse_args()
    num_expressions = args.num_expressions
    exp_in_one_line = 4
    exps = ''
    with open('exp_file.txt', 'w') as f:
        for i in range(num_expressions):
            while True:
                exp = generate_expression()
                if exp:
                    exps += f'{exp:<20}'
                    break
            if (i + 1) % 4 == 0:
                print(exps, file=f)
                exps = ''
        if exps:
            print(exps, file=f)