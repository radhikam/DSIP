from pylab import *
a = imread('Images/BnWFlower.jpg')
aa = double(a)
c = 255 #for 8 bit image
b = c-a
figure(1)
subplot(1,2,1)
gray()
imshow(aa)
title('Original B/W Image')
subplot(1,2,2)
gray()
imshow(b)
title('Image Negative')
show()

