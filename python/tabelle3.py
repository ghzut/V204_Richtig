import numpy as np
x, y, z = np.genfromtxt('data3.txt', unpack=True)

ca= 400
r= 8000
d= 0.03
n= 5
k= [0] * n
a= [0] * n
b= [0] * n
c= [0] * n
for i in range(n):
    a[i]=x[i] * 200 /3.3
    b[i]=y[i] * 10 /2.25
    c[i]=z[i] * 10 /2.25
    e=b[i]/c[i]
    g=np.log(e)
    zaehler= r * ca * d**2
    nenner=2 * a[i] * g
    k[i] = zaehler/nenner
    print('Kappa: ', k[i])
print(a)
m = np.sum(k) / len(k)
f = 0
for i in range(n):
    f = f + np.sqrt((k[i]-m)**2)
f = f/np.sqrt(n*(n-1))
print('Der Mittelwert von Kappa ist:', m)
print('Der Fehler von Kappa ist:', f)
