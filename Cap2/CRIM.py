import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Carregar dados
data_url = "http://lib.stat.cmu.edu/datasets/boston"
boston = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)
X = np.hstack([boston.values[::2, :], boston.values[1::2, :2]])
y = boston.values[1::2, 2]

# Selecionar as quatro características: 'CRIM', 'NOX', 'RM', 'AGE'
A = X[:, [0, 4, 5, 6]]
b = y

# Ajustar o modelo de regressão linear
model = LinearRegression()
model.fit(A, b)

# Obter o vetor de peso
weights = model.coef_

# Resultados
print("Vetor de peso (coeficientes):", weights)
print("Intercepto:", model.intercept_)