import sys
import numpy as np
import matplotlib.pyplot as plt
from time import time

def main():
    l = float(sys.argv[1])
    g = 9.8


    u1 = float(sys.argv[2])
    u2 = float(sys.argv[3])
    x = u1+0.5
    h = 0.2
    tet= np.zeros(100)
    w= np.zeros(100)


    def fun(y): 
        return -(g/l)*np.sin(y)


    def rungeKutta(u10, u20, x, h):  
        #valor inicial de y
        u2 = u20
        u1 = u10
        n = (int)((x - u1)/h) #número de pasos

        #iteraciones
        for i in range(1, n + 1): 
            #u2 es $\omega$ w
            #calculo de las pendientes
            #u1 es $\theta$
            k1= h * u2
            l1 = h * fun(u1) 
            k2= h * (u2 + 0.5*l1)
            l2 = h * fun(u1 + 0.5 * k1) 
            k3= h * (u2 + 0.5*l2)
            l3 = h * fun(u1 + 0.5 * k2)
            k4= h * (u2 + l3)
            l4 = h * fun(u1 + k3) 
            #valor de u1(i+1)
            u1 = u1 + (1.0 / 6.0)*(k1 + 2 * k2 + 2 * k3 + k4)
            #valor de u1(i+1)
            u2 = u2 + (1.0 / 6.0)*(k1 + 2 * k2 + 2 * k3 + k4)
            
        return u1,u2

    for i in range(100):
        tet[i] = rungeKutta(u1, u2, x, h)[0]
        w[i]= rungeKutta(u1, u2, x, h)[1]
        u1=rungeKutta(u1, u2, x, h)[0]
        u2= rungeKutta(u1, u2, x, h)[1]
        x=u1+0.5
        
    plt.plot(tet,w)
    plt.title('Velocidad angular vs posición angular')
    plt.ylabel(r'$\omega$')
    plt.xlabel(r'$\theta$')
    plt.show()

if __name__ == "__main__":
    main()