# Mesh-Optimizer
Using a distortion formula (which measures the "non-symmetry" of a discretization of a continuous space with triangles) we can minimize via the Newton-Raphson
method the distortion and thus maximize the symmetry. Mainly useful for numerical methods in PDEs.
For poligonalizations which aren't triangles the formula of distortion must be modified, otherwise you just need to modify which points you will be using for the
discretization in the matrix X inside mesh.py and the connections in the matrix T inside mesh.py (which determine the polygons). 
