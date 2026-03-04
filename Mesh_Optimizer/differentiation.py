import numpy as np

def gradient_num(func, x_val):
    n = len(x_val)
    grad = np.zeros(n)
    eps = 4.64e-6
    
    # Càlcul vectorial de l'increment
    dx = eps * np.maximum(np.abs(x_val), 0.5)
    
    for i in range(n):
        x_orig = x_val[i]
        
        x_val[i] = x_orig + dx[i]
        f_plus = func(x_val)
        
        x_val[i] = x_orig - dx[i]
        f_minus = func(x_val)
        
        grad[i] = (f_plus - f_minus) / (2 * dx[i])
        x_val[i] = x_orig
        
    return grad

def hessian_num(func, x_val):
    n = len(x_val)
    H = np.zeros((n, n))
    eps = 1e-4
    dx = eps * np.maximum(np.abs(x_val), 0.5)
    
    f_val = func(x_val)
    
    for i in range(n):
        xi_orig = x_val[i]
        
        x_val[i] = xi_orig + dx[i]
        f_plus = func(x_val)
        
        x_val[i] = xi_orig - dx[i]
        f_minus = func(x_val)
        
        H[i, i] = (f_plus - 2 * f_val + f_minus) / (dx[i]**2)
        x_val[i] = xi_orig
        
        for j in range(i):
            xj_orig = x_val[j]
            
            x_val[i] = xi_orig - dx[i]
            x_val[j] = xj_orig - dx[j]
            f_mm = func(x_val)
            
            x_val[i] = xi_orig + dx[i]
            x_val[j] = xj_orig - dx[j]
            f_pm = func(x_val)
            
            x_val[i] = xi_orig - dx[i]
            x_val[j] = xj_orig + dx[j]
            f_mp = func(x_val)
            
            x_val[i] = xi_orig + dx[i]
            x_val[j] = xj_orig + dx[j]
            f_pp = func(x_val)
            
            H[i, j] = (f_pp - f_pm - f_mp + f_mm) / (4 * dx[i] * dx[j])
            H[j, i] = H[i, j]
            
            x_val[i] = xi_orig
            x_val[j] = xj_orig
            
    return H
            
            x[i] = xi_ini
            x[j] = xj_ini
    return H

