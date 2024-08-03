from sklearn.datasets import load_digits
import numpy as np

# Carregar os dados da imagem MNIST
X = load_digits().data

# 1) Encontrar a semelhança entre a primeira imagem e a décima imagem usando dot product
primeira_imagem = X[0]
decima_imagem = X[9]

similaridade_primeira_decima = np.dot(primeira_imagem, decima_imagem)
print("Semelhança entre a primeira e a décima imagem:", similaridade_primeira_decima)

# 2) Encontrar a semelhança para uma combinação de todas as imagens usando o dot product de forma eficiente
# A multiplicação de matrizes de X por sua transposta nos dará uma matriz de semelhança
matriz_semlhanca = np.dot(X, X.T)

print("Matriz de semelhança (primeiras 5x5 entradas):\n", matriz_semlhanca[:5, :5])
