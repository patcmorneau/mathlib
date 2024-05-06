import sys, os
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__), 
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)
from mathlib import mathlib
import numpy as np
import matplotlib.pyplot as plt

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


normal = mathlib.fit_plane(points)
#print(normal)
xx,yy,zz = get_surface(normal, points[0])



fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(xx, yy, zz, alpha=0.5, rstride=100, cstride=100, color='g', label='Plane')

ax.quiver(points[0,0], points[0,1], points[0,2], normal[0], normal[1], normal[2], length=0.5, normalize=True, color='r', label='Normal')

x = points[:,0]
y = points[:,1]
z = points[:,2]

ax.scatter(x, y, z)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
