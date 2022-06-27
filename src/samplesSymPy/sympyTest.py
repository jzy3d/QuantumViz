from sympy import *



x, y, z = symbols('x y z', real=True)
f = 4*x*y + x*sin(z) + x**3 + z**8*y


diffOnX = diff(f, x)

print(diffOnX)


x = symbols('x')
a = Integral(cos(x)*exp(x), x)

init_session() # to print in console
Eq(a, a.doit())

print(a.doit())