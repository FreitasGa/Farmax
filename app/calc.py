from sympy import *

def calcPrecoMax(preco):

    x = symbols('x') #atribuir a variavel x como sendo uma variavel matematica da funcao
    c = 50000 + 80*x + 0.003*x**2 # funcao custo genérica
    r = preco * x # função receita
    l = r - c #lucro

    init_printing(use_unicode=True) # iniciando o sympy
    d1 = diff(l, x) # Derivada da função custo

    max = solve(d1, x) # resolvendo a equação
    max =  max[0] # Pegando a raiz positiva da funcao
    max = Integer(max)

    return max;

