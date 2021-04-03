import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

mpl.rcParams['legend.fontsize'] = 10

fig = plt.figure()
ax = fig.gca(projection='3d')
x = np.linspace(-5, 5, 1000)
y = np.linspace(-5, 5, 1000)
x, y = np.meshgrid(x, y)
z=abs((y-2))+(x+1)**2+3

#Find the minimum with Nelder-mead method
from scipy.optimize import minimize

def zed(param):
    x0,y0=param
    return abs((y0-2))+(x0+1)**2+3
x0 = [0, 0]



res = minimize(zed, x0, method='Nelder-Mead')
print(res)
#print(z,min(z))


#function view
ax.plot_wireframe(x, y, z, rstride=10, cstride=10,label='z',alpha=.05)
plt.xlabel("x")
plt.ylabel("y")
#plt.zlabel("z")
plt.title("z =  abs((y0-2))+(x0+1)**2+3")
#minimum converted back to x and y
ax.scatter(res.x[0],res.x[1],zed((res.x[0],res.x[1])),label="minimum",c="r",alpha=.5,s=5)

#different guess
x0=[.121214125,2]
res = minimize(zed, x0, method='Nelder-Mead')
ax.scatter(res.x[0],res.x[1],zed((res.x[0],res.x[1])),label="different guess",c="black",alpha=.5)


print("the minimun is successfully located using different starting guessses. It is",res.x[0],res.x[1],"with a z value of",zed((res.x[0],res.x[1])))
ax.legend()
plt.show()
