from sympy import *


def calc_price(price):
    # atribuir a variavel x como sendo uma variavel matematica da funcao
    x = symbols('x')
    c = 50000 + 80 * x + 0.003 * x ** 2  # funcao custo genérica
    r = price * x  # renda
    l = r - c

    # iniciando o sympy, n sei se é realmente necessario
    init_printing(use_unicode=True)
    d1 = diff(l, x)  # Derivada da função custo

    max = solve(d1, x)  # resolvendo a equação
    max = max[0]  # Pegando
    max = Integer(max)

    return max