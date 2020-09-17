#!/usr/bin/env python
# coding: utf-8

# In[35]:


import numpy as np       #Importamos numpy para el uso de funciones trigonometricas y raíces

class VectorCartesiano:

    def __init__(self, x, y, z):   #Los objetos son instanciados junto con sus componentes cartesianas
        self.x = x                 #Se defininen sus componentes cartesianas como atributos
        self.y = y  
        self.z = z
        self.Norma = np.sqrt(x**2 + y**2 + z**2)     #Se define su norma como atributo
        
    def Esfericas(self):                    #Se crea el metodo que calcula y da atributos de componentes esféricas
        self.r = np.sqrt(self.x**2 + self.y**2 + self.z**2)
        if np.fabs(self.x) < 1e-7:
            self.phi = np.pi/2
        else:
            self.phi = np.arctan(self.y/self.x)%(2*np.pi)
        
        if np.fabs(self.r) < 1e-7:
            self.theta = 0
            
        else:
            self.theta = np.arccos(self.z/self.r)%(np.pi)

        
        return VectorPolar(self.r,self.theta,self.phi)   #Se retorna un objeto de la clase VectorPolar
    
    def Print(self):
        '''Imprime el vector'''
        print(f"[{self.x},{self.y},{self.z}]")         #Metodo de coordenadas de vector
        
    def __mul__(self,other):                           #Sobrecarga de multiplicación producto punto, se devuelve un 
        '''Sobrecarga del operador suma'''             #float
        return self.x*other.x+self.y*other.y+self.z*other.z
    
    def Cruz(self,other):                              #Metodo de producto cruz, se devuelve un VectorCartesiano
        return VectorCartesiano(self.y*other.z - self.z*other.y,-(self.x*other.z-self.z*other.x),self.x*other.y-self.y*other.x)
    
    def __add__(self, other):                          #Metodo de suma, se devuelve un VectorCartesiano  
        return VectorCartesiano(self.x+other.x,self.y+other.y,self.z+other.z)
    
    def __sub__(self, other):                         #Metodo de resta, se devuelve un VectorCartesiano
        return VectorCartesiano(self.x-other.x,self.y-other.y,self.z-other.z)
    
    
    def __eq__(self, other):                          #Metodo de igualdad, se devuelve true cuando se cumple
                                                      #False cuando no
        if self.x == other.x and self.y==other.y and self.z==other.z:
            return True
        else:
            return False
     
    def __getitem__(self,key):                       #Metodo de obtener item
        return getattr(self,key)

    
    
class VectorPolar(VectorCartesiano):                #Se hereda de la clase VectorCartesiano
    
    def __init__(self, r, theta, phi):              #Se instancia propiamente creando atriutos de coordenadas esfericas
        if r >= 0:
            self.r=r
            self.theta=theta%np.pi
            self.phi=phi%(2*np.pi)                  #Se instancia tambien su versión cartesiana para tener sus atributos
                                                    #Como magnitud y componentes cartesianas
            VectorCartesiano.__init__(self,self.r*np.sin(self.theta)*np.cos(self.phi),self.r*np.sin(self.theta)*np.sin(self.phi),r*np.cos(self.theta))
        else:
            print('Ingrese un valor positivo de r')
            
    def Cartesianas(self):                          #Se crea un metodo que retorne este vector pero cartesiano
        print('Las coordenadas cartesianas son: (%.0f,%.0f,%.0f)'%(self.x,self.y,self.z))
        return VectorCartesiano(self.x,self.y,self.z)

