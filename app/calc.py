from sympy import init_printing, symbols, diff, Integer, solve

def calcMin(preco):
    x = symbols('x')
    custo =  0.003*x**2 + 80*x + 50000
    receita = preco * x
    lucro = receita - custo

    init_printing(use_unicode=True)
    d1 = diff(lucro, x)
    min = solve(d1, x)
    min = Integer(min)

    return lucro, min

def calcMax(preco):
    x = symbols('x')
    custo =  -0.003*x ** 2 + 80 * x + 50000
    receita = preco * x
    lucro = receita - custo

    init_printing(use_unicode=True)
    d1 = diff(lucro, x)

    max = solve(d1, x)
    max = max[0]
    max = Integer(max)

    return lucro, max