# programa para calcular el area y el perimetro de un circulo

# libreria
import math 
# ------------
# input 
# ------------

print ("------------")
print ("area y perimetro del circulo")
print ("------------")

r= input ("digite el valor del radio: ")
r= int(r)

# --------
# processing 
# --------
a= math.pi*r**2
p= 2*math.pi*r

# output
print ("-------------")
print ("---resultados---")
print ("-------------")
print (" El área del circulo es: " + str(a))
print ("El perimetro del circulo es: " + str(p))
print ("---------------")
