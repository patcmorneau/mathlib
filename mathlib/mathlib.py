import numpy as np
import math
import cv2 as cv

def is_inside_rectangle(rect:list, point:list)->bool :
	if point[0] < rect[0] :
		return False
	elif point[1] < rect[1] :
		return False
	elif point[0] > rect[2] :
		return False
	elif point[1] > rect[3] :
		return False
	return True

def gen_rotation_matrix(angle:int):
	rotation_matrix = np.array([[math.cos(math.radians(angle)),math.cos(math.radians(angle+90))],[math.sin(math.radians(angle)),math.sin(math.radians(angle+90))]])
	return rotation_matrix



def find_min_distance_pts_p(points:list, point:list)->list:
	diff = np.array(points) - np.array(point)
	#print(np.array(points))
	# Find the distance of point from all points
	diffNorm = np.linalg.norm(diff, 2, 1)
	#print(diffNorm[np.argmin(diffNorm)]
	# Find the index with minimum distance and return it
	ans = np.argmin(diffNorm)
	#print(points[ans])
	return points[ans]

def delaunay_triangulation(subdiv, points):
	
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
	
def calculate_center(pointList:list)->tuple:
	x = 0
	y = 0
	
	for point in pointList:
		x += point[0]
		y += point[1]
	centerX = x/len(pointList)
	centerY = y/len(pointList)
	return (int(centerX),int(centerY))

def unit_vector(vector:np.ndarray)->np.ndarray:
    """ Returns the unit vector of the vector.  """
    return vector / np.linalg.norm(vector)

def angle_between(a:np.ndarray, b:np.ndarray)->int:
	# a and b are vectors
	inner = np.dot(a,b)
	norms = np.linalg.norm(a) * np.linalg.norm(b)
	cos = inner / norms
	rad = np.arccos(cos)
	deg = np.rad2deg(rad)
	if(cos < 0):
		deg = 180 - deg
	return deg
	
def triangulate(points:list)->list:
	x = np.array(points)
	x = x.flatten()
	topLeft = min(x)
	bottomRigh = max(x)
	
	rect = [topLeft, topLeft, bottomRigh, bottomRigh]
	subdiv = cv.Subdiv2D(rect)
	for point in points:
		subdiv.insert(point)
	
	return subdiv.getTriangleList()


def decimal2angular(angle:float)->str:
	"""
	if latitude < 0 :
		latitude = abs(latitude)
		directiony = "S"
	else :
		directiony = "N"
	"""
	deg = int(angle)
	temp = 60 * (angle - deg)
	minutes = int(temp)
	seconds = int(60 * (temp - minutes))
	
	return '{}°{}’{}’’'.format(deg, minutes, seconds)
					
def angular2decimal(angle:str)->float: 
	temp = angle.split("°")
	integer = float(temp[0])
	del temp[0]
	x = temp[0]
	temp = x.split("’")
	minutes = float(temp[0])
	secondes = float(temp[1])
	
	return integer + (secondes/3600) + (minutes/60)
	
	

x = angular2decimal("47°56’13’’")
print(x)

"""
x = decimal2angular(47.937)
print(x)
"""
