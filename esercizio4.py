print("\n\n --------ESERCIZIO 4---------")

import numpy as np
M=np.loadtxt("M4.txt",dtype='i',delimiter=' ')
print("matrice di riferimento\n ",M)
aval,avec= np.linalg.eig(M)
autovalori= np.linalg.eigvals(M)
print("gli auovettori sono rispettivamente \n", avec)
print("gli autovalori ottenuti con le due funzioni sono\n", aval,autovalori)