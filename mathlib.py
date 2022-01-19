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

def find_min_distance_pts_p(points, point):
	diff = np.array(points) - np.array(point)
	#print(np.array(points))
	# Find the distance of point from all points
	diffNorm = np.linalg.norm(diff, 2, 1)
	#print(diffNorm[np.argmin(diffNorm)]
	# Find the index with minimum distance and return it
	ans = np.argmin(diffNorm)
	#print(points[ans])
	return points[ans]

def delaunay_triangulation( subdiv, points):
	
	face_triangulated = []
	# Obtain the list of triangles.
	# Each triangle is stored as vector of 6 coordinates
	# (x0, y0, x1, y1, x2, y2)
	triangleList = subdiv.getTriangleList();

	# Will convert triangle representation to three vertices pt1, pt2, pt3
	for t in triangleList :
		t_pt1 = (t[0], t[1])
		t_pt2 = (t[2], t[3])
		t_pt3 = (t[4], t[5])

		# Find the landmark corresponding to each vertex
		landmark1 = find_min_distance_pts_p(points,t_pt1)
		landmark2 = find_min_distance_pts_p(points,t_pt2)
		landmark3 = find_min_distance_pts_p(points,t_pt3)
		delaunay_triangle = [landmark1, landmark2, landmark3]
		face_triangulated.append(list(delaunay_triangle))
	return face_triangulated
