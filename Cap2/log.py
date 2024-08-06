from sympy import *

# Definindo as variáveis simbólicas
x, a, b, k = symbols('x a b k')
aaa
# Definindo as funções
f1 = x**3 - 1
f2 = log(x**2 - 3*k)
f3 = exp(a*x**b)

# Calculando as derivadas
df1dx = diff(f1, x)
df2dx = diff(f2, x)
df3dx = diff(f3, x)

# Imprimindo as derivadas
print("Derivada de f1:", df1dx)
print("Derivada de f2:", df2dx)
print("Derivada de f3:", df3dx)
