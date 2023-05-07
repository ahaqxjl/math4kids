from flask import Flask, render_template, request


app = Flask(__name__)


def generate_expression_response(generate_expression, request):
    num_expressions = int(request.args.get('num_expressions'))
    exps = []
    for i in range(num_expressions):
        while True:
            exp = generate_expression()
            if exp and exp not in exps:
                exps.append(f'{exp}')
                break

    # print(exps)
    return render_template('expressions.html', exps=exps)


@app.route('/')
def hello():
    # return '<h1>Hello, World!</h1>'
    return render_template('math4kids.html')

@app.route('/twodigitsplus1digitcarry')
def twodigtisplus1digitcarry():
    from math_exp_generator.twodigitsplus1digitcarry import generate_expression
    return generate_expression_response(generate_expression, request)

@app.route('/calculateunder20')
def calculateunder20():
    from math_exp_generator.calculateunder20 import generate_expression
    return generate_expression_response(generate_expression, request)

@app.route('/plusunder10')
def plusunder10():
    from math_exp_generator.plusunder10 import generate_expression
    return generate_expression_response(generate_expression, request)

@app.route('/minusunder10')
def minusunder10():
    from math_exp_generator.minusunder10 import generate_expression
    return generate_expression_response(generate_expression, request)

@app.route('/calculateunder10')
def calculateunder10():
    from math_exp_generator.calculateunder10 import generate_expression
    return generate_expression_response(generate_expression, request)

@app.route('/plusunder20')
def plusunder20():
    from math_exp_generator.plusunder20 import generate_expression
    return generate_expression_response(generate_expression, request)

@app.route('/minusunder20')
def minusunder20():
    from math_exp_generator.minusunder20 import generate_expression
    return generate_expression_response(generate_expression, request)