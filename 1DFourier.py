from pylab import *
u = arange(-5,5,0.01)
A = int(raw_input("enter the amplitude"))
X = int(raw_input("enter the length"))
a = sin(pi*X*u)
b = pi*X*u
F = (A*X)*(a/b)
figure(1)
subplot(1,1,1)
plot(u,F)
ylim(0,20)
title('1 D Fourier Transform')
ylabel('Amplitude')
show()
