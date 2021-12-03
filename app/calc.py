from sympy import init_printing, symbols, diff, Integer, solve

def calcMax(price):
    x = symbols('x')

    price = int(price)
    cost = -0.003 * x ** 2 + 80 * x + 50000
    receipt = price * x
    profit = receipt - cost

    init_printing(use_unicode=True)
    d1 = diff(profit, x)

    max = solve(d1, x)
    max = max[0]
    max = int(max)

    return abs(max)
