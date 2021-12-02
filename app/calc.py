from sympy import *

def calcPreço(preco):

    x = symbols('x') #atribuir a variavel x como sendo uma variavel matematica da funcao
    c = 50000 + 80*x + 0.003*x**2 # funcao custo genérica
    r = preco * x # renda
    l = r - c

    init_printing(use_unicode=True) # iniciando o sympy, n sei se é realmente necessario
    d1 = diff(l, x) # Derivada da função custo

    max = solve(d1, x) # resolvendo a equação
    max =  max[0] #Pegando
    max = Integer(max)

    return max;

