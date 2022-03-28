print("\n\n --------ESERCIZIO 2 --------")

def med_dev(list):
   import math
   result=[]
   med=0.0
   med2=0.0
   for i in list:
     med2=med2+i**2/len(list)
     med=med+i/len(list)
   result.append(med)
   result.append(math.sqrt(med2-med**2))
   return result
     

import numpy as np
filename="es2data.txt"
a=np.loadtxt(filename,skiprows=1,usecols=range(0,5))
#print(a)
#print(a[:,2])
#print(a[:,3])
tmin=[]
tmax=[]
years=[]
for i in range(0,len(a[:,2])):
   tmin.append(a[i,2])
   tmax.append(a[i,3])
   years.append(int(a[i,0]))
#print("tmin",tmin)
#print("tmax",tmax)
print("Calcolo da funzioni di NUMPY \n temperatura minima: media", np.mean(a[:,2]),"deviazione standard", np.std(a[:,3]), "\n temperatura massima: media",np.mean(a[:,3]), "deviazione standar", np.std(a[:,3]))
r_tmin=med_dev(tmin)
r_tmax=med_dev(tmax)
print("Calcolo da funzioni handmade \n temperatura minima: media",r_tmin[0],"deviazione standard", r_tmin[1], "\n temperatura massima: media",r_tmax[0], "deviazione standar", r_tmax[1])
import matplotlib.pyplot as plt
plt.plot(years,tmin,color='green',label="T min")
plt.plot(years,tmax,color='red',label="T max")
plt.title("Temperatura minima e massima negli anni")
plt.xlabel("Anno")
plt.ylabel("T")
plt.legend()
plt.show(block=False)