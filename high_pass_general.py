from pylab import *
aa = imread('Images/BnWFlower.jpg')
a = double(aa)
row,col = a.shape
m = input('enter the mask: ')
w = empty([m,m])
for i in range(1,m):
    for j in range(1,m):
        w[i,j] = -1
s = (m+1)/2
w[s,s] = (m**2)-1
b = empty([row,col])
for x in range(1,row):
    for y in range(1,col):
        b[x,y] = a.item(x,y)
for x in range(s,row-s):
    for y in range(s,col-s):
        b[x,y] = 0
for x in range(s,row-s):
    for y in range(s,col-s):
        for i in range(1,m):
            for j in range(1,m):
                b[x,y] = a.item(x-s+i,y-s+j)*w.item(i,j)+b.item(x,y)
        if b.item(x,y) < 0:
            b[x,y] = 0
n = 0
for x in range(s,row-s):
    for y in range(s,col-s):
        if b.item(x,y) > n:
            n = b.item(x,y)
c = 255/n
for x in range(s,row-s):
    for y in range(s,col-s):
        b[x,y] = c*b.item(x,y)
figure(1)
subplot(1,2,1)
gray()
imshow(aa)
title('Original Image')
subplot(1,2,2)
gray()
imshow(uint8(b))
title('Image after high pass filter')
show()       
