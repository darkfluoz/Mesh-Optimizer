import numpy as np
import matplotlib.pyplot as plt

# 6 nodes interiors + 14 nodes frontera = 20 nodes
N_INT = 6

# Coordenades explícites de la malla. 
# Els primers 6 són els interiors (descol·locats a propòsit perquè l'optimitzador treballi).
# Els últims 14 formen un perímetre rectangular perfecte.
X_nodes = np.array([
    # --- Nodes interiors (Distorsionats) ---
    [0.5, 0.5],  # Node 0 (La posició òptima serà 1,1)
    [2.5, 0.8],  # Node 1 (La posició òptima serà 2,1)
    [3.5, 1.5],  # Node 2 (La posició òptima serà 3,1)
    [0.8, 2.5],  # Node 3 (La posició òptima serà 1,2)
    [2.2, 1.8],  # Node 4 (La posició òptima serà 2,2)
    [2.8, 2.8],  # Node 5 (La posició òptima serà 3,2)
    
    # --- Nodes de la frontera (Fixos) ---
    [0.0, 0.0], [1.0, 0.0], [2.0, 0.0], [3.0, 0.0], [4.0, 0.0], # 6 a 10 (A baix)
    [4.0, 1.0], [4.0, 2.0], [4.0, 3.0],                         # 11 a 13 (Dreta)
    [3.0, 3.0], [2.0, 3.0], [1.0, 3.0], [0.0, 3.0],             # 14 a 17 (A dalt)
    [0.0, 2.0], [0.0, 1.0]                                      # 18 a 19 (Esquerra)
], dtype=float)

# 24 Triangles connectant els nodes
T_elements = np.array([
    [6, 7, 0], [6, 0, 19],     # Quadrat 1 (A baix - esquerra)
    [7, 8, 1], [7, 1, 0],      # Quadrat 2
    [8, 9, 2], [8, 2, 1],      # Quadrat 3
    [9, 10, 11], [9, 11, 2],   # Quadrat 4 (A baix - dreta)
    [19, 0, 3], [19, 3, 18],   # Quadrat 5
    [0, 1, 4], [0, 4, 3],      # Quadrat 6 (Centre)
    [1, 2, 5], [1, 5, 4],      # Quadrat 7
    [2, 11, 12], [2, 12, 5],   # Quadrat 8
    [18, 3, 16], [18, 16, 17], # Quadrat 9 (A dalt - esquerra)
    [3, 4, 15], [3, 15, 16],   # Quadrat 10
    [4, 5, 14], [4, 14, 15],   # Quadrat 11
    [5, 12, 13], [5, 13, 14]   # Quadrat 12 (A dalt - dreta)
], dtype=int)

def mostra_malla(X, titol="Malla"):
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    # Canviem l'estil perquè es vegi exactament com el teu original
    ax.triplot(X[:, 0], X[:, 1], T_elements, 'k*-', lw=1.0)
    ax.plot(X[:N_INT, 0], X[:N_INT, 1], 'ro', label='Nodes interiors')
    ax.set_title(titol)
    plt.show()

def empaqueta_dofs(X_in):
    return X_in[:N_INT, :].flatten()

def desempaqueta_dofs(vec_y):
    X_nova = np.copy(X_nodes)
    X_nova[:N_INT, :] = vec_y.reshape((N_INT, 2))
    return X_nova
