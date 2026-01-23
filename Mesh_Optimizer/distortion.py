import numpy as np
import matplotlib.pyplot as plt

A = np.array([[1, -np.sqrt(3.) / 3], [0, 2 * np.sqrt(3.) / 3]],dtype=float)

def calculaDistorsioTriangle(Xe):
  etat = 0.0
  Dphi = np.array([Xe[1,:]-Xe[0,:], Xe[2,:]-Xe[0,:]]).T
  Dphi = Dphi@A
  detDphi = np.linalg.det(Dphi)
  frobDphi = np.linalg.norm(Dphi,'fro')
  etat = (frobDphi**2)/(2*abs(detDphi))
  return etat

def calculaDistorsioMalla(X, T):
    eta = 0.0
    for e in range (T.shape[0]): #0,...,Nint-1 són els nodes interiors
      Xe = X[T[e,:],:]
      eta += calculaDistorsioTriangle(Xe)**2
    return np.sqrt(eta)

