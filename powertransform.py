from pylab import *
aa = imread('Images/BnWFlower2.jpeg')
a = double(aa)
row,col,d = a.shape
b = empty([row,col,d])
m = int(raw_input('Enter the correction factor:'))
for x in range(1,row,1):
    for y in range(1,col,1):
        for z in range(1,d,1):
            c = a.item(x,y,z)**m
            b[x,y,z] = c
numax = b.max()
numin = b.min()
n = 255/(numax-numin)
nuimg1 = empty([row,col,d])
for x in range(1,row):
    for y in range(1,col):
        for z in range(1,d):
            nuimg1[x,y,z] = n*(b.item(x,y,z)-numin)
nuimg2 = uint8(nuimg1)
figure(1)
subplot(1,2,1)
gray()
imshow(aa)
title('OriginalImage')
subplot(1,2,2)
imshow(nuimg2)
title('Image after Power Transformation')
show()


