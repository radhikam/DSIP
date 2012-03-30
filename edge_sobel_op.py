from pylab import *
aa = imread('Images/BnWFlower.jpg')
a = double(aa)
row,col = a.shape
w1 = array([[-1,-2,-1],[0,0,0],[1,2,1]])
w2 = array([[-1,0,1],[-2,0,2],[-1,0,1]])
a1 = a2 = empty([row,col])

for x in range(2,row-1):
    for y in range(2,col-1):
        a1[x,y] = w1.item(0,0)*a.item(x-1,y-1) + w1.item(0,1)*a.item(x-1,y) + w1.item(0,2)*a.item(x-1,y+1) + w1.item(1,0)*a.item(x,y-1) + w1.item(1,1)*a.item(x,y) + w1.item(1,2)*a.item(x,y+1) + w1.item(2,0)*a.item(x+1,y-1) + w1.item(2,1)*a.item(x+1,y) + w1.item(2,2)*a.item(x+1,y+1)
        a2[x,y] = w2.item(0,0)*a.item(x-1,y-1) + w2.item(0,1)*a.item(x-1,y) + w2.item(0,2)*a.item(x-1,y+1) + w2.item(1,0)*a.item(x,y-1) + w2.item(1,1)*a.item(x,y) + w2.item(1,2)*a.item(x,y+1) + w2.item(2,0)*a.item(x+1,y-1) + w2.item(2,1)*a.item(x+1,y) + w2.item(2,2)*a.item(x+1,y+1)
a3 = a1 + a2
figure()
subplot(2,2,1)
gray()
imshow(aa)
title('Original Image')
subplot(2,2,2)
gray()
imshow(uint8(a1))
title('X-Gradient Image')
subplot(2,2,3)
gray()
imshow(uint8(a2))
title('Y-Gradient Image')
subplot(2,2,4)
gray()
imshow(uint8(a3))
title('Rsultant Image')
show()
