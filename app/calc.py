from sympy import *

#-----------------------------------------------

priceUni = 200; # Aqui vai ser o input do preco do remedio!

#-----------------------------------------------
#Aqui comeca a magica heheheheh

x = symbols('x')
c = 50000 + 80*x + 0.003*x**2 # custo
r = priceUni * x # renda
l = r - c

init_printing(use_unicode=True) # iniciando o sympy, n sei se é realmente necessario
d1 = diff(l, x) # primeira derivada dos crias! Amém :)

max = solve(d1, x) # resolvendo a equação
max =  max[0] #Pegando
max = Integer(max) # valor da unidade que deve serr fabricada para obter o lucro maximo

#-----------------------------------------------
