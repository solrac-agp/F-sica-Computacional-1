#!/usr/bin/env python
# coding: utf-8

# In[4]:


import vector as v
import numpy as np
a = v.VectorCartesiano(1.5,0,2.4)
b = v.VectorCartesiano(0,1,9)
c = v.VectorCartesiano(4.2,0.05,0)

aE = a.Esfericas()
print('Las coordenadas esféricas de a son: (%f, %f, %f)'%(aE.r,aE.theta,aE.phi))
bE = b.Esfericas()
print('Las coordenadas esféricas de b son: (%f, %f, %f)'%(bE.r,bE.theta,bE.phi))
cE = c.Esfericas()
print('Las coordenadas esféricas de c son: (%f, %f, %f)'%(cE.r,cE.theta,cE.phi))
apuntob = a*b
print('El producto punto a*b es: %f'%apuntob)
apuntoc = a*c
print('El producto punto a*c es: %f'%apuntoc)
bpuntoc = b*c
print('El producto punto b*c es: %f'%bpuntoc)
acruzb = a.Cruz(b)
print('El producto cruz axb es: (%f,%f,%f)'%(acruzb.x,acruzb.y,acruzb.z))
acruzc = a.Cruz(c)
print('El producto cruz axc es: (%f,%f,%f)'%(acruzc.x,acruzc.y,acruzc.z))
bcruzc = b.Cruz(c)
print('El producto cruz bxc es: (%f,%f,%f)'%(bcruzc.x,bcruzc.y,bcruzc.z))
angab = np.arccos(apuntob/(a.Norma*b.Norma))
print('El ángulo entre a y b es: %f radianes o %f grados'%(angab,angab*180/np.pi))
angac = np.arccos(apuntoc/(a.Norma*c.Norma))
print('El ángulo entre a y c es: %f radianes o %f grados'%(angac,angac*180/np.pi))
angbc = np.arccos(bpuntoc/(b.Norma*c.Norma))
print('El ángulo entre b y c es: %f radianes o %f grados'%(angbc,angbc*180/np.pi))

