from matplotlib import pyplot as plt



x = [5,6,7,8]
y = [7,3,8,3]

x2 = [1,3,5,7]
y2 = [6,7,2,6]

plt.plot(x,y, 'c', linewidth = 5, label = 'line One')
plt.plot(x2,y2, 'r', linewidth = 10, label = 'line Two')

plt.title("EPIC CHART")
plt.xlabel('X-axis')
plt.ylabel('Y-axis')



plt.legend()

plt.show()
