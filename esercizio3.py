print("\n\n-----ESERCIZIO 3-----") 

import numpy as np
el=[]
for i in range(5):
 new=input("inserisci elemento  ")
 new=int(new)
 el.append(new)
e=np.array(el)
print("creo un array in 1D",e)

a=np.array([[1,2,3,6],[5,6,7,9],[1,9,8,4]])
print("\ncreo un array 3D:\n",a)
print("\nelemento 1,1:",a[1][1])
print("elemento  2,1:",a[2,1])
print("elemento 2,2:", a[2][2])
print("\nslicing \nprinto il minore 2x2 in alto a dx", a[0:2,0:2])
print("seconda colonna", a[:][1])
print("ultima riga", a[2])

b=e.copy() 
b=b*3
print("b:",b,"e:",e)
c=e 

for i in range(len(c)):
  c[i]=c[i]*3
print("c:",c,"e:",e)

d=np.array([3,6,1,5,3])
print("\nsomma ",e+d)
print("sottrazione",d-e)
print("prodotto elemento per elemento",e*d)
print("prodotto scalare",np.dot(e,d))