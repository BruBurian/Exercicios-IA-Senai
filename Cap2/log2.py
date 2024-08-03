from sympy import *

# Definindo as variáveis simbólicas e a função
x, y = symbols('x y')
f = exp(x**2 + 2*y**2)

# Calculando as primeiras derivadas parciais
df_dx = diff(f, x)  # Derivada em relação a x
df_dy = diff(f, y)  # Derivada em relação a y

# Calculando as segundas derivadas parciais
df2_dx2 = diff(f, x, 2)  # Segunda derivada em relação a x
df2_dy2 = diff(f, y, 2)  # Segunda derivada em relação a y
df2_dxy = diff(f, x, y)  # Derivada mista

# Imprimindo os resultados
print("f_x =", df_dx)
print("f_y =", df_dy)
print("f_xx =", df2_dx2)
print("f_yy =", df2_dy2)
print("f_xy =", df2_dxy)