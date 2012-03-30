from pylab import *
aa = imread('Images/BnWPebbles.jpg')
a = double(aa)
row,col,d = a.shape
m = input('enter the mask size')
n = m**2
w = empty([m,m,m])
for i in range(1,m):
    for j in range(1,m):
        for k in range(1,m):    
            w[i,j,k] = 1/n
s = (m+1)/2
b = empty([row,col,d])
for x in range(1,row):
    for y in range(1,col):
        for z in range(1,d):
            b[x,y,z] = a.item(x,y,z)       
for x in range(s,row-s):
    for y in range(s,col-s):
        for z in range(s,d-s):
            b[x,y,z] = 0
c = empty([row,col,d])
for x in range(s,row-s,1):
    for y in range(s,col-s,1):
        for z in range(s,d-s,1):
            for i in range(1,m):
                for j in range(1,m):
                    for k in range(1,m):
                        c[x,y,z] = a.item(x-s+i,y-s+j,z-s+k)*w.item(i,j,k)+b.item(x,y,z)
subplot(2,1,1)
imshow(aa)
title('Original Image')
subplot(2,1,2)
gray()
imshow(uint8(b))
title('Low Pass Filtered Image')
show()

