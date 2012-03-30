from pylab import *
a = imread('Images/a.jpg')
p = double(a)
r = int(raw_input('enter the bit you want to see 1=MSB and 8=LSB'))
row,col,d = a.shape
b = w = empty([row,col,d])
z = p.size
c = empty([z])
for i in range(1,row):
    for j in range(1,col):
        for k in range(1,d):
            x = int(p.item(i,j,k))
            c = bin(x)
            b[i,j,k] = c[r]
            w = b
            #w[i,j,k] = double(b.item(i,j,k))
            if w.item(i,j,k)== 48: #or w(i,j,k) == 49:
                w[i,j,k]=255
            else:
                w[i,j,k]=0
figure(1)
subplot(1,2,1)
gray()
imshow(a)
title('Original Image')
subplot(1,2,2)
imshow(uint(w))
title('Bit Plane Slicing')
show()
