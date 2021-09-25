import numpy as np
from vpython import *



# plot
pos_graf = graph(title="posisjon mot tid", xtitle="t (s)", ytitle="pos (m)", fast=False)
pos_curve = gcurve(graph=pos_graf)
vel_graf = graph(title="hastighet mot tid", xtitle="t (s)", ytitle="v (m/s)", fast=False)
vel_curve = gcurve(graph=vel_graf)
fnet_graf = graph(title="Netto kraft mot tid", xtitle="t (s)", ytitle="Fnet (N)", fast=False)
fnet_curve = gcurve(graph=fnet_graf)

# konstanter
g = vec(0,-9.81,0)           #m/s^2
m = 0.5             #kj
D = 0.5
rho = 1.30

# overflate areal
A = 0.8 

# initialbetingelser
pos = vec(0,0,0)    
vel = vec(0,0,0)

# tidsbetingelser
t = 0 
dt = 0.1
tmax = 10 



while t < tmax:
     
     t += dt
     
     # Regner ut kreftene
     Fg = -m*g
     Fr = D*rho*A*(vel.mag2*vec(0,1,0))/2
     
     # sumen av kreftene
     Fnet = Fg + Fr
     
     # lagrer tidligere posisjon
     tidligere_pos = pos
     
     # Eulers-cromers metode for å oppdatere fart og posisjon
     vel = vel + (Fnet / m) * dt
     pos = pos + vel * dt
     
     
     pos_curve.plot(t, pos.y)
     vel_curve.plot(t, vel.y)
     fnet_curve.plot(t, Fnet.y)



     


