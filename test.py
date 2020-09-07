#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Este archivo buscar probar todas las funciones 
import funciones as f
f_1 = f.Factorial(5)
f_2 = f.Factorial(10)

b_1=f.Binomial(10,5)
b_2=f.Binomial(10,10)
b_3=f.Binomial(10,0)

f.Pascal(4)

print('El factorial de 5 es %.0f'%f_1)
print('El factorial de 10 es %.0f'%f_2)
print('El coeficiente binomial (10,5) es %.0f'%b_1)
print('El coeficiente binomial (10,10) es %.0f'%b_2)
print('El coeficiente binomial (10,0) es %.0f'%b_3)
print('Se le ha guardado un archivo llamado Pascal-5.txt con el trigulo de pascal para n=4')

