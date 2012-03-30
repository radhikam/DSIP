from pylab import *
aa = imread('Images/color.jpeg')
a = double(aa)
row,col,d = a.shape
h = zeros(300)
for n in range(1,row):
    for m in range(1,col):
        for l in range(1,d):
            if a.item(n,m,l)==0:
                a[n,m,l] = 1
for n in range(1,row):
    for m in range(1,col):
        for l in range(1,d):
            t = a.item(n,m,l)
            h[t] = h.item(t)+1
figure(1)
subplot(1,2,1)
gray()
imshow(aa)
title('Original Image')
subplot(1,2,2)
hist(h)
title('Histogram')
show()
