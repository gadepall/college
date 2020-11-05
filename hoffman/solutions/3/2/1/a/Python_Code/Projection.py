import matplotlib.pyplot as plt

x1 = [1,2]
y1 = [3,4]
x2 = [2,4]
y2 = [1,3]
x3 = [1,2]
y3 = [0,0]
x4 = [1,1]
y4 = [3,0]
x5 = [2,2]
y5 = [4,0]
plt.scatter(x1,y1,color='r',zorder=2)
plt.plot(x1,y1,'r')
plt.plot(x4,y4,'b--')
plt.plot(x5,y5,'b--')
plt.scatter(x3,y3,color='b',zorder=2)
plt.plot(x3,y3,'b')
plt.annotate(" A ",(1,3))
plt.annotate(" B", (2,4))
plt.annotate(" A' ",(1,0))
plt.annotate(" B' ", (2,0))
plt.xlim(-1, 5)
plt.ylim(-1, 5)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Projection of  line AB on to x axis')
#plt.legend()
plt.grid()
plt.show()
plt.savefig("Projection.png")
