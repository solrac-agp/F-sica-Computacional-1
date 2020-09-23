#!/usr/bin/env python
# coding: utf-8

# In[113]:


import matplotlib.pyplot as plt
import numpy as np


class Oscilador:


    def __init__(self, m, k, y0, t):   #Los objetos son instanciados junto con sus componentes cartesianas
        self.m = m                 
        self.k = k  
        self.y0 = y0
        self.w0 = np.sqrt(k/m)
        self.T=np.linspace(0,t,t*1000)
        self.X=y0*np.cos(self.w0*self.T)
        self.V=-self.w0*self.y0*np.sin(self.w0*self.T)


        
        
    def XvsT(self):
        plt.plot(self.T,self.X,label='$m = %.0f$, $k = %.0f$, $y_0 = %.0f$, $\omega_0 = %.2f$'%(self.m,self.k,self.y0,self.w0))
        
    def VvsT(self):
        plt.plot(self.T,self.V,label='$m = %.0f$, $k = %.0f$, $y_0 = %.0f$, $\omega_0 = %.2f$'%(self.m,self.k,self.y0,self.w0))
    
    #def fig(self):
     #   plt.figure(figsize(15,10))
        
    
        
    def show(self,xq,xunit,yq,yunit,tit):
        self.xunit=xunit
        self.xq=xq
        self.yq=yq
        self.yunit=yunit
        self.tit=tit
        
        plt.ylabel(f"${self.yq} \ ({self.yunit})$",fontsize=20)
        plt.xlabel(f"${self.xq} \ ({self.xunit})$",fontsize=20)
        plt.title(f"Gráfica de {self.tit}", fontsize=20)

        
        plt.grid()
        plt.legend(fontsize=8, loc='best')
        plt.show()
        
class OsciladorAmortiguado(Oscilador):
    
    def __init__(self, m, k, y0, b, t):   #Los objetos son instanciados junto con sus componentes cartesianas
        self.m = m                 
        self.k = k  
        self.y0 = y0
        self.w0 = np.sqrt(k/m)
        self.b = b
        self.lamb = self.b/(2*self.m)
        if self.lamb < self.w0:
            self.T=np.linspace(0,t,t*1000)
            self.X=y0*np.cos(self.w0*self.T)*np.exp(-self.lamb*self.T)
            self.V=-self.y0*np.exp(-self.lamb*self.T)*(self.lamb*np.cos(self.w0*self.T) + self.w0*np.sin(self.w0*self.T))
        else:
            print('Ingrese párametros del caso subamortiguado')

