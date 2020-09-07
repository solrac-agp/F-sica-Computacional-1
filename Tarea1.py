#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Imporemos el módulo que hemos creado:

import funciones as f

# Hagamos los cálculos:

# P1 denotará la probabilidad de que tirada 100 veces la moneda resulte 10 veces cara:

P1 = f.Binomial(100,10)*(1/(2**100))

# P2 denotará la probabilidad de que tras tirada 100 veces la moneda resulte más de 30 veces cara
# Para este cálculo lo que debemos es sumar sobre la probabilidad de cada número de veces que caiga cara mayor a 30

P2 = 0
for i in range(31,101):
    P2 += f.Binomial(100,i)*(1/(2**100))
    
# Imprimamos estos resultados

print('La probabilidad de que caiga cara 10 veces después de haber tirado la moneda 100 veces es de %.9f'%P1)
print('La probabilidad de que caiga cara más de 30 veces después de haber tirado la moneda 100 veces es de %.9f'%P2)


# In[ ]:




