print("--------ESERCIZIO 1--------")

def crea_istogramma (file_name):
 indata=open(file_name,'r')
 val=[int(x) for x in 
 next(indata).split()]
 indata.close()
 print("lista dei valori",val)
 for i in val:
   print("#"*i, "\n")

def crea_istogramma_grafico(file_name):
  
 import matplotlib.pyplot as plt
 import numpy as np
 indata=open(file_name,'r')
 val=[int(x) for x in next(indata).split()]
 indata.close()
 print("lista di valori",val)
 plt.hist(np.arange(0,len(val),1),weights=val,orientation='horizontal')
 plt.gca().invert_yaxis()
 plt.show(block=False)

crea_istogramma('es1data.txt')
crea_istogramma_grafico('es1data.txt')