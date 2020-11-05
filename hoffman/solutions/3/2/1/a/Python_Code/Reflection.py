import matplotlib.pyplot as plt

x1 = [1,3]
y1 = [2,4]
x2 = [0,5]
y2 = [0,5]
x3 = [2,4]
y3 = [1,3]
plt.scatter(x1,y1,color='r',zorder=2)
plt.scatter(x3,y3,color='b',zorder=2)
plt.plot(x1,y1,'r')
plt.plot(x2,y2,'y--',label= 'y = x')
plt.plot(x3,y3,'b')
plt.annotate(" A(1,2) ",(1,2))
plt.annotate(" B (3,4)", (3,4))
plt.annotate(" A'(2,1) ",(2,1))
plt.annotate(" B' (4,3)", (4,3))
plt.xlim(0, 5)
plt.ylim(0, 5)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Reflection of line AB about the diagonal x = y')
plt.legend()
plt.grid()
plt.show()

