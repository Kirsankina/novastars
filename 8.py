import matplotlib.pyplot as pl
import matplotlib.patches as mpatches
import matplotlib.path as mpath
import matplotlib.lines as mlines
import math
import os
import numpy as np
from astropy.io import ascii
from matplotlib import rc, rcParams
import matplotlib.font_manager
from matplotlib.lines import Line2D
from matplotlib.collections import PatchCollection

rcParams['font.size'] = 18
rcParams['lines.linewidth'] = 3
rcParams['lines.markersize'] = 3
rcParams['grid.linestyle'] = '--'
rcParams['axes.titlepad'] = 18
rcParams['xtick.direction'] = 'in'
rcParams['ytick.direction'] = 'in'
rcParams['xtick.top'] = True
rcParams['ytick.right'] = True
rcParams['font.family'] = 'serif'
rcParams['mathtext.fontset'] = 'dejavuserif'
rc('legend', fontsize=15)
rc('xtick.major', size=5, width=1.5)
rc('ytick.major', size=5, width=1.5)
rc('xtick.minor', size=3, width=1)
rc('ytick.minor', size=3, width=1)



def EX1():
	stars = ['0.82mdot8', '0.82mdot9', '1.0mdot9']
	labels = [r'M=0.82, $\frac{dM}{dt}=10^{-8}$', r'M=0.82, $\frac{dM}{dt}=10^{-9}$', r'M=1.0, $\frac{dM}{dt}=10^{-9}$']
	col = ['r-', 'b-', 'g-']
	ci = 0
	for S in stars:
	    name = 'C:/University/NOVA/M'+S+'/LOGS/history.data'
	    data = ascii.read(name, header_start=4, data_start=5)
	    t = data['star_age']
	    lgL = data['log_L']
	    lgR = data['log_R_cm']
	    lgTeff = data['log_Teff']
	    Mdot = data['star_mdot']
	    for j in range(len(t)):
	        #t[j] = np.log10(t[j])
	        Mdot[j] = np.log10(Mdot[j])
	    Y = [lgL, lgR, lgTeff, Mdot]
	    ylab = [r'$\log(L), L_{\odot}$', r'$\log(R)$, см', r'$\log(Teff), K$', r'$\frac{dM}{dt}, M_{\odot}$ в год']
	    titles = [r'Светимость от времени', r'Радиус от времени', r'Эффективная температура от времени', r'Темп потери массы от времени']
	    for k in range(4):
	        pl.figure(k)
	        pl.grid(k+1)
	        pl.plot(t, Y[k], label = labels[ci])
	        pl.xlabel('t, years')
	        pl.ylabel(ylab[k])
	        pl.title(titles[k])
	#        pl.text(t[0], Y[k][0], S)
	        pl.legend(loc = 'best')
	    ci += 1
	for k in range(4):
	    pl.show(k) 

def EX2():
	Mass = '1.38'
	mdot = 'mdot10'
	name = 'C:/University/NOVA/M'+Mass+mdot+'/LOGS/history.data'
	data = ascii.read(name, header_start=4, data_start=5)
	t = data['star_age']
	lgL = data['log_L']
	pl.plot(t, lgL, 'b-')
	pl.xlabel('t, years')
	pl.ylabel('log(L), Lsun')
	pl.title(Mass+'_'+mdot)
	pl.show()


def EX3():
	P = [7071, 106693, 1075425, 1753, 29176, 453410, 175, 3952,
	     61664, 38.4, 534, 5376]
	M = [0.82, 0.82, 0.82, 1, 1, 1, 1.3, 1.3, 1.3, 1.38, 1.38, 1.38]
	Mdot = [1e-8, 1e-9, 1e-10, 1e-8, 1e-9, 1e-10, 1e-8, 1e-9, 1e-10, 1e-8, 1e-9, 1e-10]
	critM = []
	for j in range(12):
	    critM.append(math.log10(Mdot[j]*P[j]))
	    P[j] = math.log10(P[j])
	    print(math.pow(10, critM[j]))
	pl.figure(0)
	pl.plot([0.82, 1, 1.3, 1.38], [P[0], P[3], P[6], P[9]], '-o', alpha = 0.7, label = 'dM/dt=1e-8', markersize = 10)
	pl.plot([0.82, 1, 1.3, 1.38], [P[1], P[4], P[7], P[10]], '-o', alpha = 0.7, label = 'dM/dt=1e-9', markersize = 10)
	pl.plot([0.82, 1, 1.3, 1.38], [P[2], P[5], P[8], P[11]], '-o', alpha = 0.7,label = 'dM/dt=1e-10', markersize = 10)
	pl.xlabel(r'$M, M_{\odot}$')
	pl.ylabel(r'$\log(P)$, годы')
	pl.title(r'Зависимость периода от начальной массы звезды')
	pl.legend(loc = 'best')
	pl.grid()
	pl.show(0)
	pl.figure(1)
	pl.plot([1e-8, 1e-9, 1e-10], [P[0], P[1], P[2]], '-o', alpha = 0.7,label = 'M=0.82', markersize = 10)
	pl.plot([1e-8, 1e-9, 1e-10], [P[3], P[4], P[5]],'-o', alpha = 0.7, label = 'M=1.0', markersize = 10)
	pl.plot([1e-8, 1e-9, 1e-10], [P[6], P[7], P[8]], '-o', alpha = 0.7, label = 'M=1.3', markersize = 10)
	pl.plot([1e-8, 1e-9, 1e-10], [P[9], P[10], P[11]], '-o', alpha = 0.7, label = 'M=1.38', markersize = 10)
	pl.xlabel(r'$\frac{dM}{dt}, M_{\odot}$ в год')
	pl.ylabel(r'$\log(P)$, годы')
	pl.title(r'Зависимость периода от темпа акреции')
	pl.xlim((0,1.2e-8))
	pl.legend(loc = 'best')
	pl.grid()
	pl.show(1)
	pl.figure(2)
	pl.plot([0.82, 1, 1.3, 1.38], [critM[0], critM[3], critM[6], critM[9]], '-o', alpha = 0.7, label = 'dM/dt=1e-8', markersize = 10)
	pl.plot([0.82, 1, 1.3, 1.38], [critM[1], critM[4], critM[7], critM[10]], '-o', alpha = 0.7, label = 'dM/dt=1e-9', markersize = 10)
	pl.plot([0.82, 1, 1.3, 1.38], [critM[2], critM[5], critM[8], critM[11]], '-o', alpha = 0.7,label = 'dM/dt=1e-10', markersize = 10)
	pl.xlabel(r'$M, M_{\odot}$')
	pl.ylabel(r'$\log(P*\frac{dM}{dt})$')
	pl.title(r'Зависимость критической массы от начальной массы звезды')
	pl.legend(loc = 'best')
	pl.grid()
	pl.show(2)
	pl.figure(3)
	pl.plot([1e-8, 1e-9, 1e-10], [critM[0], critM[1], critM[2]], '-o', alpha = 0.7, label = 'M=0.82', markersize = 10)
	pl.plot([1e-8, 1e-9, 1e-10], [critM[3], critM[4], critM[5]], '-o', alpha = 0.7, label = 'M=1.0', markersize = 10)
	pl.plot([1e-8, 1e-9, 1e-10], [critM[6], critM[7], critM[8]], '-o', alpha = 0.7,label = 'M=1.3', markersize = 10)
	pl.plot([1e-8, 1e-9, 1e-10], [critM[9], critM[10], critM[11]], '-o', alpha = 0.7, label = 'M=1.38', markersize = 10)
	pl.xlabel(r'$\frac{dM}{dt}, M_{\odot}$ в год')
	pl.ylabel(r'$\log(P*\frac{dM}{dt})$')
	pl.title(r'Зависимость критической массы от темпа акреции')
	pl.xlim((0,1.2e-8))
	pl.legend(loc = 'best')
	pl.grid()
	pl.show(3)	

def EX4():
	P = [7071, 106693, 1075425, 1753, 29176, 453410, 175, 3952,
	     61664, 38.4, 534, 5376]
	M = [0.82, 0.82, 0.82, 1, 1, 1, 1.3, 1.3, 1.3, 1.38, 1.38, 1.38]
	Mdot = [1e-8, 1e-9, 1e-10, 1e-8, 1e-9, 1e-10, 1e-8, 1e-9, 1e-10, 1e-8, 1e-9, 1e-10]
	critM = []
	col=['C0', 'C1', 'C2']
	for j in range(12):
		critM.append(math.log10(Mdot[j]*P[j]))
	stars =  ['M0.82mdot9', 'M1.0mdot9']  #['M0.82mdot8',
	Nfiles = ['M1.38mdot8']#,'M1.0mdot9','M1.3mdot9','M1.38mdot8']
	#Список, состоящий из цветов, обозначающих параметры
	#Col = ['b','g','y','r']
	#Col = ['r']
	pp = 'C:/University/NOVA/'
	for i in range(len(stars)):
	    name = pp+stars[i]+'/LOGS/history.data'

	    data = ascii.read(name, header_start=4,data_start=5)
	    lgt = data['star_age']
	    m = data['star_mass']
	    
	    pl.plot(lgt,m, '-o',color = col[i], alpha = 0.7, label = stars[i])
	    # if i == 0:
	    # 	pl.plot(5, critM[0], 'o', markersize = 10)
	    # elif i == 1:
	    # 	pl.plot(5, critM[1], 'o', markersize = 10)
	    # elif i == 2:
	    # 	pl.plot(5, critM[4], 'o', markersize = 10)

	pl.title(r'Зависимость массы звезды от времени')
	pl.xlabel(r'Время, годы')
	pl.ylabel(r'Масса, $M_{\odot}$')
	pl.legend(loc = 'best')
	pl.grid()
	pl.show()



EX1()	
EX2()
EX3()
EX4()
