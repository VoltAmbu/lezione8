print("\n\n-----ESERCIZIO 3-----") 

import numpy as np
el=[]
for i in range(5):
 new=input("inserisci elemento  ")
 new=int(new)
 el.append(new)
e=np.array(el)
print("ho creato un array 1D a partire da una lista dettata dall'utente",e)

a=np.array([[1,2,3,6],[5,6,7,9],[1,9,8,4]])
print("\nho creato un array 3d:\n",a)
print("indicizzazione\nprinto elemento 1,1:",a[1][1])
print("printo elemento  2,1:",a[2,1])
print("printo elemento 2,2", a[2][2])
print("\nslicing \nprinto il minore 2x2 in alto a dx", a[0:2,0:2])
print("printo la seconda colonna", a[:][1])
print("printo la l'ultima riga", a[2])



b=e.copy() #  COPIA ELEMENTO PER ELEMENTO questo comando crea un array b con elementi uguali agi elementi di e. I due array si riferiscono a celle di memoria diverse "
b=b*3
print("b:",b,"e:",e)
c=e #  COPIA PER RIFERIMENTO questo comando crea un array c che si riferisce alle stesse celle di memoria a cui si rifereisce e. Se il contenuto delle celle di memoria di c viene modificato, lo stesso accade anche al vettore e, che ha celle uguali. "

for i in range(len(c)):
  c[i]=c[i]*3
print("c:",c,"e:",e)


d=np.array([3,6,1,5,3])
print("\nsomma ",e+d)
print("sottrazione",d-e)
print("prodotto elemento per elemento",e*d)
print("prodotto scalare",np.dot(e,d))