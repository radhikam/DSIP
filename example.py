def binto8(x,y):
    #code to make a binary number 8 bit binary
    n = bin(int(x))
    m = list(n)
    count = len(m) - 2
    for i in range(0,count):
        m.insert(2,0)
        m = m[y+1]
    return m
# x=no. in the image array here p.item(x,y), y=r    

