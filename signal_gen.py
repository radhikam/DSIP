from pylab import *
subplot(2,2,1)
x = arange(1,20,1)
y = x.copy()
plot(x,y,'r')
title('$Unit Step Sjgnal$')
xlabel('$x$')
ylabel('$y$')

subplot(2,2,2)
x = arange(1,20,1,dtype=type(int()))
y = x
scatter(x,y)
title('$Unit Ramp$')
xlabel('$x$')
ylabel('$y$')

subplot(2,2,3)
a = int(raw_input('enter a value for exponential signal:'))
x = arange(1,20,0.05)
y = a**x
plot(x,y,'g')
title('$Exponential$')
xlabel('$x$')
ylabel('$y$')


subplot(2,2,4)
x = arange(1,20,0.05)
plot(x,sin(x),'r')
title('$Sin(x)$')
xlabel('$x$')
ylabel('$y$')

show()



