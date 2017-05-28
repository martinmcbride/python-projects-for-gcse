import matplotlib.pyplot as plt

xvalues = []
yvalues = []
x = -0.1
y = 0

for i in range(1000):
    xvalues.append(x)
    yvalues.append(y)
    x, y = 1 - y + abs(x), x

plt.plot(xvalues, yvalues, 'bo')
plt.show()