import matplotlib.pyplot as plt

values = []
x = 1

for i in range(10):
    values.append(x)
    x = -x

plt.plot(values)
plt.plot(values, 'bo')
plt.show()