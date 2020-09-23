#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import MasaResorte as MS
O1=MS.Oscilador(1,1,1,20)
O2=MS.Oscilador(1,10,2,20)
O3=MS.Oscilador(1,2,4,20)
O4=MS.Oscilador(5,3,7,20)
O5=MS.Oscilador(10,2,6,20)
#O1.fig()
O1.XvsT()
O2.XvsT()
O3.XvsT()
O4.XvsT()
O5.XvsT()
O1.show('Tiempo','s','Elongación','m','posición contra tiempo sin amortiguación')
#O1.fig()
O1.VvsT()
O2.VvsT()
O3.VvsT()
O4.VvsT()
O5.VvsT()
O1.show('Tiempo','s','Velocidad','m/s','Velocidad contra tiempo sin amortiguación')
O6=MS.OsciladorAmortiguado(1,1,1,0.1,30)
O7=MS.OsciladorAmortiguado(1,1,1,0.1,30)
O8=MS.OsciladorAmortiguado(1,10,2,0.1,30)
O9=MS.OsciladorAmortiguado(1,2,4,0.1,30)
O10=MS.OsciladorAmortiguado(5,3,7,0.1,30)

#O6.fig()
O6.XvsT()
O7.XvsT()
O8.XvsT()
O9.XvsT()
O10.XvsT()
#O2.XvsT()
O6.show('Tiempo','s','Elongación','m','posición contra tiempo caso subamortiguado $b=0.1 kg/s$')
#O3.fig()
O6.VvsT()
O7.VvsT()
O8.VvsT()
O9.VvsT()
O10.VvsT()
#O2.VvsT()
O6.show('Tiempo','s','Velocidad','m/s','Velocidad contra tiempo caso subamortiguado $b=0.1 kg/s$')

