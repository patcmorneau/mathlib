import matplotlib.pyplot as plt
import numpy as np
import math

#vector = np.array([5,2])
#print(vector)

def is_inside_rectangle(rect, point) :
	if point[0] < rect[0] :
		return False
	elif point[1] < rect[1] :
		return False
	elif point[0] > rect[2] :
		return False
	elif point[1] > rect[3] :
		return False
	return True

def gen_rotation_matrix(angle):
	rotation_matrix = np.matrix([[math.cos(math.radians(angle)),math.cos(math.radians(angle+90))],[math.sin(math.radians(angle)),math.sin(math.radians(angle+90))]])
	return rotation_matrix

#matrix_rotation = gen_rotation_matrix(90)

#print(matrix_rotation)

#ans = matrix_rotation.dot(vector)

#print(ans)

"""
# plotting the graph
ax = plt.quiver(x_coordinate, y_coordinate,x_direction, y_direction,units='xy', scale=1)
plt.grid()
plt.ylim(-10,10)
plt.xlim(-10,10)
plt.show()
"""
