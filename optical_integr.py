#Интегрирование точного решения кинетик затухания люминесценции символьным методом
#Из за сложности получаемых уравнений. Последующий подбор коэффициентов методом МНК
# и печать результата
#

import sympy as sym


def del_flu_sym(x ,t = 1 ,Ka = 1, Ktt = 0.5):
    intens = x**2
    return intens


x = sym.Symbol('x')
t = sym.Symbol('t')
dlfl_integral = sym.integrate(del_flu_sym(x, t), (x))
print(dlfl_integral(2))
sym.pprint(dlfl_integral)
