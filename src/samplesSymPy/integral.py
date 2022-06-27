from sympy import *
from python_latex import *


x = symbols('x')
a = Integral(cos(x)*exp(x), x)

init_session() # to print in console
Eq(a, a.doit())

