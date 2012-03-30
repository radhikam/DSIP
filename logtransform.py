from pylab import *
aa = imread('Images/BnWFlower.jpg')
a = double(aa)
row,col = a.shape
c = a
for x in range(1,row,1):
    for y in range(1,col,1):
        c[x,y]=a.item(x,y)*((1)^(x+y))
b = abs(fft2(c))
b_log=log(1+b)
#plotting
figure(1)
subplot(2,2,1)
gray()
imshow(aa)
subplot(2,2,2)
gray()
imshow(b)
subplot(2,2,3)
gray()
imshow(b_log)
show()
