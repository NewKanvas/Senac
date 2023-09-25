from artimetica import multiplicacao as mult

x = [1,2,3,4,5,6,7,8,9,10]
y = [11,12,13,14,15,16,17,18,19,20]
xy = []

for i in range(len(x)):
    xy.append(mult(x[i],y[i]))

print(xy)