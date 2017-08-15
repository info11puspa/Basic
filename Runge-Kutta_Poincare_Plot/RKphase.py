'''@SL Nov 28 2015'''
import numpy as np
import sympy as s
import matplotlib.pyplot as plt
class driven_pendulum:
    def __init__(self,q,a,w_d):
        self.q = q
	self.a = a
	self.w_d = w_d
    def RK_4(self):
      k = []
      g = []
      omega = [0]
      th = [0]
      tht = [0]
      oma = [0]
# number of time intervals for the calculation

      for i in range(500):
#      for i in np.arange(0,20000,2*np.pi/self.w_d):
        tfiless = []
#stepsize h:

        h = 1/100.
	#h = 2*np.pi/(300.*self.w_d)
	tfiles = i
#Each time interval is further divided into 100 parts

       	for i in range(100):
        
	    tfiles +=h
	    tfiless.append(tfiles)
	thetafiless = [tht[0]]
	omegafiless = [oma[0]]
#Defining a iterative function that calculates k_0,k_1.....

	def f(t,theta,w):
		kk = h*w
	        gg = h*((-1/self.q)* w - np.sin(theta) + self.a*np.cos(self.w_d *t))
	        k.append(kk)
		g.append(gg)
        # 0<= t <= 2pi/w_d
        #N = 20
	#1. d (theta)/d t = w
	#2. d (w)/d t = -1/q w - sin(theta) + a cos(w_d t)
        
#loop for succesive calculation of theta and omega:

        for i in range(len(tfiless)):
	    f(tfiless[i],thetafiless[i],omegafiless[i])
	    f(tfiless[i]+h/2.,thetafiless[i]+float(k[0])/2.,omegafiless[i]+float(g[0])/2.)
	    f(tfiless[i]+h/2.,thetafiless[i]+float(k[1])/2.,omegafiless[i]+float(g[1])/2.)
	    f(tfiless[i]+h/2.,thetafiless[i]+float(k[2]),omegafiless[i]+float(g[2]))
	    tt = (thetafiless[i]+(1/6.)*(k[0]+2*k[1]+2*k[2]+k[3]))
	    thetafiless.append(tt)
	    ww = omegafiless[i]+(1/6.)*(g[0]+2*g[1]+2*g[2]+g[3])
	    omegafiless.append(ww)
	    k = []
	    g = []
	th.append(float('%.6f'%(thetafiless[-1])))
	omega.append(float('%.6f'%(omegafiless[-1])))
	tht = []
	oma = []
	tht.append(thetafiless[-1])
	oma.append(omegafiless[-1])
	omegafiless = []
	thetafiless = []


      th = np.array(th)
      omega = np.array(omega)
#      print th[150:]
#      print omega[150:]
 #wrapper for theta between -pi to pi.

      for i in range(len(th)):
	  while th[i]>np.pi:
	        th[i] -=2*np.pi
	  while th[i] < -np.pi:
	        th[i] +=2*np.pi

      plt.plot(th[150:],omega[150:],':',lw = 1)
     


