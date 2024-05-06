import sys, os
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__), 
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)
from mathlib import mathlib
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.transform import Rotation

def get_surface(normal, point_on_plane, size=1):
	xx, yy = np.meshgrid(np.arange(point_on_plane[0] - size, point_on_plane[0] + size, 0.1),
						np.arange(point_on_plane[1] - size, point_on_plane[1] + size, 0.1))
	zz = (-normal[0] * xx - normal[1] * yy) / normal[2]
	
	return xx,yy,zz


points = np.array([
	[1, 0, 0],
	[2, 0, 0],
	[3, 0, 0],
	[4, 0, 0],
	[5, 0, 0],
	[0, 1, 0],
	[0, 2, 0],
	[0, 3, 0],
	[0, 4, 0],
	[0, 5, 0]
])

R = Rotation.from_euler('zyx', [45,0,0], degrees=True).as_matrix()

points2 = np.dot(points, R)


normal = mathlib.fit_plane(points)
normal2 = mathlib.fit_plane(points2)
#print(normal)
xx,yy,zz = get_surface(normal, points[0])
xx2,yy2,zz2 = get_surface(normal2, points2[0])



fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(xx, yy, zz, alpha=0.5, rstride=100, cstride=100, color='g', label='Plane')
ax.plot_surface(xx2, yy2, zz2, alpha=0.5, rstride=100, cstride=100, color='b', label='Plane2')

ax.quiver(points[0,0], points[0,1], points[0,2], normal[0], normal[1], normal[2], length=0.5, normalize=True, color='r', label='Normal')
ax.quiver(points2[0,0], points2[0,1], points2[0,2], normal2[0], normal2[1], normal2[2], length=0.5, normalize=True, color='w', label='Normal2')

print(mathlib.angle_between(normal, normal2))

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
