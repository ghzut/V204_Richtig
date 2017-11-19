import numpy as np
x, y, z = np.genfromtxt('data.txt', unpack=True)

ca= 385
r= 8520
d= 0.03
n=10
k= [0] * n
a= [0] * n
b= [0] * n
c= [0] * n
for i in range(n):
    a[i]=x[i] * 100 /2.25
    b[i]=y[i] * 10 /2.2
    c[i]=z[i] * 10 /2.2
    e=b[i]/c[i]
    g=np.log(e)
    zaehler= r * ca * d**2
    nenner=2 * a[i] * g
    k[i] = zaehler/nenner
    print('Kappa: ',k[i])
m = np.sum(k) / len(k)
f = 0
for i in range(n):
    f = f + np.sqrt((k[i]-m)**2)
f = f/np.sqrt(n*(n-1))
print('Der Mittelwert von Kappa ist:', m)
print('Der Fehler von Kappa ist:', f)
