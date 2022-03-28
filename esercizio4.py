print("\n\n ----ESERCIZIO 4-----")
#per diagonalizzare una matrice si utilizza il sottomodulo linalg di numpy con  np.linalg.eig(M) trovo autovettori ed autovalori , con np.linalg.eigvals(M) trovo solo gli autovalori

import numpy as np
M=np.loadtxt("matr.txt",dtype='i',delimiter=' ')
print("matrice\n ",M)
aval,avec= np.linalg.eig(M)
autovalori= np.linalg.eigvals(M)
print("autovettori\n", avec)
print("autovalori calcolati con entrambe le funzioni\n", aval,autovalori)