from matplotlib import pyplot as plt

#from matplotlib import style
#style.use('styleName')

x = [2,4,6,8]
y = [7,3,8,3]

x2 = [1,3,5,7]
y2 = [6,7,2,6]

plt.grid(True, color = "k")

plt.scatter(x,y, color = 'g',label = "woah")
plt.bar(x2,y2, color = 'b', label = "awesome", align = "center")

plt.title("My Chart")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")


plt.legend()
plt.show()

