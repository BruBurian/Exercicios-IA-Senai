import numpy as np
from scipy.spatial.distance import cosine

# Vetores a, b e c
a = np.array([4, 5, 2, 2])
b = np.array([4, 0, 2, 0])
c = np.array([2, 2, 0, 1])

# Distâncias Euclidianas
dist_ab = np.linalg.norm(a - b)
dist_ac = np.linalg.norm(a - c)
dist_bc = np.linalg.norm(b - c)

print(f"Distância Euclidiana entre a e b: {dist_ab}")
print(f"Distância Euclidiana entre a e c: {dist_ac}")
print(f"Distância Euclidiana entre b e c: {dist_bc}")

# Distâncias do Cosseno
cos_dist_ab = cosine(a, b)
cos_dist_ac = cosine(a, c)
cos_dist_bc = cosine(b, c)

print(f"Distância do Cosseno entre a e b: {cos_dist_ab}")
print(f"Distância do Cosseno entre a e c: {cos_dist_ac}")
print(f"Distância do Cosseno entre b e c: {cos_dist_bc}")