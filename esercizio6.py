print("-------ESERCIZIO 6--------")
import numpy as np
import time
for i in range(0,100):
 a=np.ones((100,100))
 b=np.zeros((100,100))
  
f=open('M6_2.txt', 'w')
t1=time.time()
for i in range(len(a)):
   print(a[i],file=f)
t2=time.time()
f.close()
print("t per stampa:",t2-t1)

t3=time.time()
np.savetxt('M6_1.txt',b,fmt='%.0f')
t4=time.time()
print("t per stampa",t4-t3)