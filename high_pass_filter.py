from pylab import *
aa = imread('Images/BnWFlower.jpg')
a = double(aa)
row,col = a.shape
w = array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])
b = empty([row,col])
for x in range(2,row-1):
    for y in range(1,col-1):
        b[x,y] = w.item(0,0)*a.item(x-1,y-1)+w.item(0,1)*a.item(x-1,y)+w.item(0,2)*a.item(x-1,y+1)+w.item(1,0)*a.item(x,y-1)+w.item(1,1)*a.item(x,y)+w.item(1,2)*a.item(x,y+1)+w.item(2,0)*a.item(x+1,y+1)+w.item(2,1)*a.item(x+1,y)+w.item(2,2)*a.item(x+1,y+1)
figure(1)
subplot(1,2,1)
gray()
imshow(aa)
title('Original Image')
subplot(1,2,2)
gray()
imshow(uint8(b))
title('Image after using high pass filter')
show()
