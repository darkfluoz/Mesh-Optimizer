import numpy as np

# Matriu de mapeig per al triangle equilàter de referència
W = np.array([[1.0, -np.sqrt(3.0) / 3.0], 
              [0.0,  2.0 * np.sqrt(3.0) / 3.0]], dtype=float)

def distorsio_element(coords_tri):
    # Vectorització dels eixos del triangle
    J = np.array([coords_tri[1, :] - coords_tri[0, :], 
                  coords_tri[2, :] - coords_tri[0, :]]).T
    
    Dphi = J @ W
    
    # Optimització: determinant i norma de Frobenius explícita (més ràpid per matrius 2x2)
    det_Dphi = Dphi[0, 0] * Dphi[1, 1] - Dphi[0, 1] * Dphi[1, 0]
    frob_sq = np.sum(Dphi**2) 
    
    return (frob_sq**2) / (2.0 * abs(det_Dphi))

def distorsio_total(X_nodes, T_elements):
    dist_sq_sum = 0.0
    for element in T_elements:
        coords = X_nodes[element, :]
        dist_sq_sum += distorsio_element(coords)**2
        
    return np.sqrt(dist_sq_sum)
