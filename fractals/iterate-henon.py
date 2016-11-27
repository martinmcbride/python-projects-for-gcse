import matplotlib.pyplot as plt

xvalues = []
yvalues = []
x = 1.12
y = 0.09

for i in range(10):
    xvalues.append(x)
    yvalues.append(y)
    print(x, y)
    x, y = y+1-1.4*x*x, 0.3*x

plt.plot(xvalues, yvalues)
plt.plot(xvalues, yvalues, 'bo')
plt.show()