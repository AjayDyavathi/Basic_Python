from matplotlib import pyplot as plt
import numpy as np

x,y = np.loadtxt('coOrdinates.csv', unpack = True, delimiter = ',')

#x,y = np.loadtxt('coOrdinates.rtf', unpack = True, delimiter = ',')


print(x)
print(y)


plt.plot(x,y)




plt.title("My Chart")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.show()
