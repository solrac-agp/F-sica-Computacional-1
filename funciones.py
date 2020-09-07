#!/usr/bin/env python
# coding: utf-8

# In[15]:


def Factorial(n):
    m=1 #Valor inicial para el producto, de esta manera factorial de cero nos dará 1
    if isinstance(n, int) and n >= 0: #Se verifica que n es un entero positivo
        for i in range(1, n+1):
            m = m*i     #En cada paso multiplicamos por el sucesor del natural anterior
        return m        #Se obtiene, naturalmente, el factorial despues de haber hecho todos los productos
    elif isinstance(n, int) and n < 0:
        print("No basta con que su número sea un entero, ¡debe ser un natural!")  #Se excluyen enteros negativos
    else:
         print("¡Su número no es un número natural!") #Se excluyen racionales que no sean naturales
            

def Binomial(n, k):
    if isinstance(n,int) and isinstance(k,int): #Se verifica que n, k sean enteros
        if n >= 0 and k >= 0:  #Se verifica que n, k sean positivos
            if n >= k:
                return Factorial(n)/(Factorial(k)*Factorial(n-k))
            else:
                print("¡Está forzando a evaluar el factorial de un número negativo!") #Considera el caso n-k negativo
        else:
            print("¡Alguno de sus números es negativo!")  #Excluye enteros negativos
    else:
        print("¡Alguno de sus números no es un entero!")  #Excluye racionales no enteros
        
def Pascal(n):
    a=[]  #Vamos a crear primero un arreglo que tenga forma de matriz que representa el triangulo
          #En lo siguiente se llenará con ceros los espacios vacíos del triangulo y con los números correspondientes
          #los espacios no vacíos  
    for j in range(0, n+1):
        b = []  #Creamos cada fila de la matriz
        k = n-j #Definimos la cantidad de espacios vacíos a la izquierda del primer 1 
        for l in range(0,k):
            b.append(0)
        
        for i in range(0, j+1): 
        
            b.append(Binomial(j,i))  #Llenamos con los binomiales
            if i==j:
                break 
            b.append(0)
        for l in range(0,k):
            b.append(0)              #Agregamos un espacio después de cada binomial
        a.append(b)                  #Agregamos la fila correspondiente
    name = ('Pascal-%.0f.txt'%n)                  #Creamos un string para el nombre del archivo    
    out = open(name, 'w')    #Creamos el archivo .txt
    for row in a:
        for column in row:             
            if column != 0:              #Llenamos con elementos no nulos
                out.write('%d' % column)
            else:
                out.write(' ')           #Llenamos con espacios
        out.write('\n')
    out.close()

