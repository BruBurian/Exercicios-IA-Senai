import numpy as np

# Vetor zerado
vetor_zerado = np.zeros(5)
print("Vetor zerado:\n", vetor_zerado)

# Vetor com uns
vetor_uns = np.ones(5)
print("\nVetor com uns:\n", vetor_uns)

# Matriz quadrada
matriz_quadrada = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\nMatriz quadrada:\n", matriz_quadrada)

# Matriz diagonal
matriz_diagonal = np.diag([1, 2, 3])
print("\nMatriz diagonal:\n", matriz_diagonal)

# Matriz identidade
matriz_identidade = np.eye(3)
print("\nMatriz identidade:\n", matriz_identidade)

# Matriz simétrica
matriz_simetrica = np.array([[1, 2, 3], [2, 4, 5], [3, 5, 6]])
print("\nMatriz simétrica:\n", matriz_simetrica)
