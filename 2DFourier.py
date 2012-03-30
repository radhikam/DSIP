from pylab import *
import mpl_toolkits.mplot3d.axes3d as p3
A = int(raw_input('Enter the amplitude')) 
X = int(raw_input('Enter the x length'))
Y = int(raw_input('Enter the y length'))
u = arange(-25,25,0.5)
v = arange(-25,25,0.5)
for m in u:
    for n in v:
        a1 = sin(pi*X*u)
        b1 = pi*X*u
        a2 = sin(pi*Y*v) 
        b2 = pi*Y*v 
        f = (A*X*Y)*(a1/b1)*(a2/b2)
        m += 1
    m = 1
    n += 1
ax = p3.Axes3D(figure())
ax.plot3D(u,abs(f),abs(f))
title('2 D Fourier Transform')
xlabel('Length')
ylabel('Amplitude')
show()
