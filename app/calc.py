from sympy import *

def calcMin(preco):
    x = symbols('x') #atribuir a variavel x como sendo uma variavel matematica da funcao
    c =  0.003*x**2 + 80*x + 50000  # funcao custo genérica para valor minimo
    r = preco * x # função receita
    l = r - c #lucro

    init_printing(use_unicode=True) # iniciando o sympy
    d1 = diff(l, x) # Derivada da função custo

    min = solve(d1, x) # resolvendo a equação
    min=  min[0] # Pegando a raiz positiva da funcao
    min = Integer(min)

    return l, min

def calcMax(preco):
    x = symbols('x')
    c =  -0.003*x ** 2 + 80 * x + 50000
    r = preco * x
    l = r - c

    init_printing(use_unicode=True)
    d1 = diff(l, x)

    max = solve(d1, x)
    max = max[0]
    max = Integer(max)

    return l, max