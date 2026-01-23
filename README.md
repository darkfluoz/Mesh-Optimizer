# Mesh-Optimizer
Using a distortion formula (which measures the "non-symmetry" of a discretization of a continuous space with triangles) we can minimize via the Newton-Raphson
method the distortion and thus maximize the symmetry. Mainly useful for numerical methods in PDEs.
For poligonalizations which aren't triangles the formula of distortion must be modified, otherwise you just need to modify which points you will be using for the
discretization in the matrix X inside mesh.py and the connections in the matrix T inside mesh.py (which determine the polygons). Must take into acccount matrixes
X and T are transposed, therefore new coordinates and connections must be noted at the start of each row. It is also important to note that "N_int" represents
the number of interior nodes, and must be modified depending on the number of nodes, use the initial plot mesh to observe which nodes must be interior and which are 
exterior to determine which must appear before and after so that exterior nodes do not appear in the distortion formula. Check into the code for an example.
