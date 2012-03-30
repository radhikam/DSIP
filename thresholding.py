from pylab import *
aa = imread('Images/BnWFlower.jpg')
a = double(aa)
p = a
row,col = a.shape
t = double(raw_input('Enter the value of threshold:'))
for i in arange(1,row,1):
    for j in arange(1,col,1):
        if a.item(i,j) < t:
            p[i,j] = 0
        else:
            p[i,j] = 255
figure(1)
subplot(1,2,1)
imshow(aa)
gray()
title('Original Image')
subplot(1,2,2)
imshow(p)
gray()
title('Image after thresholding')
show()
