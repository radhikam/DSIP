from pylab import *
a = imread('Images/BnWFlower.jpg')
p = double(a)
row,col = a.shape
for i in range(1,row,1):
    for j in range(1,col,1):
        if a.item(i,j)>50 and a.item(i,j)<150:
            p[i,j]=255
        else:
            p[i,j]=a.item(i,j)
figure(1)
subplot(1,2,1)
gray()
imshow(a)
title('Original Image')
subplot(1,2,2)
gray()
imshow(p)
title('Gray Level Slicing With Background')
show()
