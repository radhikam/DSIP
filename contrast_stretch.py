from pylab import *
aa = imread('Images/BnWPebbles.jpg')
a = double(aa)
row,col,d = a.shape
LT = double(raw_input('Enter the Lower Threshold Value:'))
UT = double(raw_input('Enter the Upper Threshold Value:'))
b = empty([row,col,d])
for x in arange(1,row,1):
    for y in arange(1,col,1):
        for z in arange(1,d,1):
            if a.item(x,y,z) <= LT:
                b[x,y,z] = 0.5*a.item(x,y,z)
            elif a.item(x,y,z) <= UT:
	            b[x,y,z] = (2*(a.item(x,y,z)-LT))+(0.5*LT)
            else:
                b[x,y,z] = 0.5*(a.item(x,y,z)-UT)+(0.5*LT)+2*(UT-LT)
subplot(1,2,1)
imshow(uint8(aa))
title('Original Image')

subplot(1,2,2)
gray()
imshow(uint8(b))
title('Contrast Stretched Image')

show()
