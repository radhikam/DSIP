from pylab import *

def binto8(x,y):
    # x=no. in the image array here p.item(x,y), y=r    
    # code to make a binary number 8 bit binary and ftech the rth value from binary number
    n = bin(int(x))
    m = list(n)
    count = abs(len(m) - 2 - 8)
    for i in range(0,count):
        m.insert(2,0)
    m = m[y+1]        
    return m

a = imread('Images/BnWFlower.jpg')
p = double(a)
r = int(raw_input('enter the bit you want to see 1=MSB and 8=LSB'))
row,col = a.shape
w = empty([row,col])
for i in range(1,row):
    for j in range(1,col):
        x = int(p.item(i,j))
        m = binto8(x,r)
        w[i,j] = double(m)
        if w[i,j] == 1:
            w[i,j] = 255
        else:
            w[i,j] = 0
figure(1)
subplot(1,2,1)
gray()
imshow(a)
title('Original Image')
subplot(1,2,2)
gray()
imshow(uint8(w))
title('Bit Plane Slicing')
show()
