from pylab import *
a = array([[1,2,3,4],[2,3,4,5],[2,2,2,2],[1,1,1,1]])
row,col = a.shape
const = sqrt(a.size)
for n in range(0,row-1):
    for k in range(0,col-1):
        W[n+1,k+1] = exp(-1*2*pi*n*k/const)
X = W*a*W
f = fft2(a)
