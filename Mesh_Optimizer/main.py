import numpy as np
import matplotlib.pyplot as plt

from mesh            import X,T,Nint,plotMesh,dofsToCoords,coordsToDofs
from differentiation import derivadaNumerica,hessianaNumerica
from distortion      import calculaDistorsioMalla

# Mostrar malla inicial
plotMesh(X,'Initial mesh')

res = calculaDistorsioMalla(X, T)
print('Distorsio inicial: ',res)

# Convertir les coordenades de la malla a un vector amb dofs
y = coordsToDofs(X)
def F(y):
  return calculaDistorsioMalla(dofsToCoords(y),T)

def newton_raphson(F, y0, tol_errR, max_iter):
    y = y0
    errors = []
    for k in range(max_iter):
        Ry = derivadaNumerica(F,y)
        Hy = hessianaNumerica(F,y)
        delta = np.linalg.solve(Hy, -Ry)
        y_new = y + delta
        err = np.linalg.norm(delta, ord=2)/np.linalg.norm(y_new, ord = 2)
        errors.append(err)
        if err < tol_errR:
            return y_new, k+1, errors
        y = y_new
    raise RuntimeError("El mètode no ha convergit")

# Condicions inicials per Newton-Raphson
y0 = coordsToDofs(X)

# Executar Newton-Raphson
y_opt, iters, errors = newton_raphson(F, y0, tol_errR=5e-8, max_iter=50)

# Reconstruir la malla final
X_final = dofsToCoords(y_opt)

# Dibuixar la malla final
plotMesh(X_final, "Malla final")

# Valor del primer node interior (fila 0 de la matriu X_final)
print("Primer node interior (malla final):", X_final[0,:])

# Valor de la distorsió final
print("Distorsió final:", calculaDistorsioMalla(X_final, T))
# X = dofsToCoords(np.ones(y.shape))

for i in errors:
    plt.plot(errors)
plt.plot(np.arange(0,iters),errors, 'k*')
plt.yscale('log')  # Logaritme dels errors
plt.xlabel('Número iteracions k')
plt.ylabel('log(r^k)')
plt.show()

print("Iteracions: ", iters)
