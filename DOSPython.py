# -*- coding: utf-8 -*-
from pylab import *
import string
import re


def lectura(f):
    z=f.read()
    lista=string.split(z,'\n')
    n=len(lista)
    l1,l2,l3,l4,l5=[],[],[],[],[]
    for i in range(1,n-1):
        cadena=' '.join(lista[i].split())
        cadena1=re.sub('\s','\t',cadena)
        x=string.split(cadena1,'\t')
        a,b,c,d,e=float(x[0]),float(x[1]),(-1.)*float(x[2]),float(x[3]),(-1.)*float(x[4])
        l1.append(a)
        l2.append(b)
        l3.append(c)
        l4.append(d)
        l5.append(e)
    return l1,l2,l3,l4,l5

pdos_tot=open("phosphorene.pdos_tot","r")

Etot, DosUp, DosDw, PDosUp, PDosDw= lectura (pdos_tot)

fill(Etot, DosUp, '--g',alpha=0.5, label='Phosphorene')
fill(Etot, DosDw, '--g',alpha=0.5,)

title('Phosphorene (1x1)', size=20)
ylabel('DOS', size=30)
xlabel('eV',size=30)
hold(True)
grid(True)
y0 = plt.axhline(y=0,linewidth=2, color='k',ls='-')
l = plt.axvline(x=-1.59,linewidth=2, color='g',ls='--')
legend(loc='upper left')

text(-1.59,3, '$E_F$= -1.59 eV',fontsize=17, horizontalalignment='center', verticalalignment='center', color='g')



#contribuciones de cada átomo por orbital
pdos_atm_1s=open("phosphorene.pdos_atm#1(P)_wfc#1(s)","r")
pdos_atm_1p=open("phosphorene.pdos_atm#1(P)_wfc#2(p)","r")
pdos_atm_2s=open("phosphorene.pdos_atm#2(P)_wfc#1(s)","r")
pdos_atm_2p=open("phosphorene.pdos_atm#2(P)_wfc#2(p)","r")
pdos_atm_3s=open("phosphorene.pdos_atm#3(P)_wfc#1(s)","r")
pdos_atm_3p=open("phosphorene.pdos_atm#3(P)_wfc#2(p)","r")
pdos_atm_4s=open("phosphorene.pdos_atm#4(P)_wfc#1(s)","r")
pdos_atm_4p=open("phosphorene.pdos_atm#4(P)_wfc#2(p)","r")


E_1s, DosUp_1s, DosDw_1s, PDosUp_1s, PDosDw_1s= lectura (pdos_atm_1s)
E_1p, DosUp_1p, DosDw_1p, PDosUp_1p, PDosDw_1p= lectura (pdos_atm_1p)

E_2s, DosUp_2s, DosDw_2s, PDosUp_2s, PDosDw_2s= lectura (pdos_atm_2s)
E_2p, DosUp_2p, DosDw_2p, PDosUp_2p, PDosDw_2p= lectura (pdos_atm_2p)

E_3s, DosUp_3s, DosDw_3s, PDosUp_3s, PDosDw_3s= lectura (pdos_atm_3s)
E_3p, DosUp_3p, DosDw_3p, PDosUp_3p, PDosDw_3p= lectura (pdos_atm_3p)

E_4s, DosUp_4s, DosDw_4s, PDosUp_4s, PDosDw_4s= lectura (pdos_atm_4s)
E_4p, DosUp_4p, DosDw_4p, PDosUp_4p, PDosDw_4p= lectura (pdos_atm_4p)

plot(E_1s,DosUp_1s,'-b',label='orbitales s')
plot(E_1p,DosUp_1p,'-y',label='orbitales p')

plot(E_2s,DosUp_2s,'-b')
plot(E_2p,DosUp_2p,'y')

plot(E_3s,DosUp_3s,'-b')
plot(E_3p,DosUp_3p,'-y')

plot(E_4s,DosUp_4s,'-b')
plot(E_4p,DosUp_4p,'-y')

#plot(Etot, DosUp, '--m', label='Phosphorene')
#plot(Etot, DosDw, '--m')

hold(True)
legend(loc='upper left')




show()
pdos_tot.close()

pdos_atm_1s.close()
pdos_atm_1p.close()
pdos_atm_2s.close()
pdos_atm_2p.close()
pdos_atm_3s.close()
pdos_atm_3p.close()
pdos_atm_4s.close()
pdos_atm_4p.close()