from pylab import *
"""N = int(raw_input('Enter N:'))
fs = int(raw_input('enter fs:'))
f1 = int(raw_input('Enter f1:'))
f2 = int(raw_input('Enter f2:'))
f3 = int(raw_input('Enter f3:'))"""

N=128
f1=150
f2=450
f3=1500
#fs=8000

#n = arange(0,N-1)
n = linspace(0,N-1,50)

#signal generation
x1 = sin(2*pi*f1*n)
x2 = (0.5)*sin(2*pi*f2*n)
x3 = sin(2*pi*f3*n)

#ploting generated signals
subplot(2,3,1)
plot(n,x1)
grid()
title('Signal x1(n)')

subplot(2,3,2)
plot(n,x2,'r')
grid()
title('Signal x2(n)')

subplot(2,3,3)
plot(n,x3,'g')
grid()
title('Signail x3(n)')

#signal manipulation

subplot(2,3,4)
a = zeros(20,dtype=type(int()))
b = x1[0:30]
x1_d = concatenate((a,b))
plot(n,x1_d)
grid()
title('Signal Delayed x1(n-20)')

subplot(2,3,5)
xadd = x1+x2
plot(n,xadd,'r')
grid()
title('Signal Addition x1(n)+x2(n)')

subplot(2,3,6)
xmul = x1*x3
plot(n,xmul,'g')
grid()
title('Signal Multiplication x1(n)*x2(n)')

show()


