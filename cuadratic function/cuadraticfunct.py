import numpy as np
import matplotlib.pyplot as plt

#Primero definimos las variables de la función, tal que; 
a = float(input("valor de a: ")) 
b= float(input("valor de b: "))
c = float(input("valor de c: "))

#funcion cuadratica

def cuadratic_function(x): 
    return a * x**2 + b*x + c 

#Ahora, establecemos el rango de "x" & evaluamos en "y"

x= np.linspace(-10, 10 ,300) 
y = cuadratic_function(x)

#Por ultimo, ploteamos 

plt.figure(figsize= (8,6))
plt.plot(x , y, label=f"${a}x^2 + {b}x + {c}$", color='b')
plt.title("Cuadratic function")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(True)
plt.legend()
plt.show()

