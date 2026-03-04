import numpy as np
import matplotlib.pyplot as plt

from differentiation import gradient_num, hessian_num
from distortion import distorsio_total
from mesh import X_nodes, T_elements, N_INT, mostra_malla, empaqueta_dofs, desempaqueta_dofs

print("--- Inici de l'optimització de la malla ---")
mostra_malla(X_nodes, 'Malla Inicial Distorsionada')

dist_ini = distorsio_total(X_nodes, T_elements)
print(f'Distorsió inicial: {dist_ini:.6f}')

# Funció objectiu 
def funcio_objectiu(y):
    return distorsio_total(desempaqueta_dofs(y), T_elements)

def newton_raphson(F, y0, tol=5e-8, max_it=50):
    y_curr = y0
    historial_errors = []
    
    for k in range(max_it):
        g = gradient_num(F, y_curr)
        H = hessian_num(F, y_curr)
        
        # Resolució del sistema lineal
        delta = np.linalg.solve(H, -g)
        y_next = y_curr + delta
        
        error = np.linalg.norm(delta) / np.linalg.norm(y_next)
        historial_errors.append(error)
        
        if error < tol:
            return y_next, k + 1, historial_errors
            
        y_curr = y_next
        
    raise RuntimeError("Newton-Raphson no ha convergit en el nombre màxim d'iteracions.")

y0 = empaqueta_dofs(X_nodes)

# Executem el mètode
y_opt, iteracions, errors = newton_raphson(funcio_objectiu, y0)

X_final = desempaqueta_dofs(y_opt)

mostra_malla(X_final, "Malla Final Optimitzada")

print(f"Nodes resolts en {iteracions} iteracions.")
print(f"Distorsió final: {distorsio_total(X_final, T_elements):.6f}")
print(f"Coordenada del primer node interior optimitzat: {X_final[0,:]}")

# Gràfica d'error netejada
plt.figure()
plt.plot(range(iteracions), errors, 'k*-')
plt.yscale('log')
plt.xlabel('Número iteració k')
plt.ylabel('Error Relatiu log(r^k)')
plt.title('Convergència Newton-Raphson')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()
