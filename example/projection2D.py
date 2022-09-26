import sys, os
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__), 
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

from mathlib import mathlib
import numpy as np
import math
import matplotlib.pyplot as plt

r = 100
angles = [11, 12, 13, 14 ,15]

xs = []
ys = []

for angle in angles:
	xs.append(r * math.cos(math.radians(angle)))
	ys.append(r * math.sin(math.radians(angle)))

xs2 = np.array(xs)
ys2 = np.array(ys)

xMean = np.mean(xs2)
yMean = np.mean(ys2)

#print(xMean, yMean)

angle = math.degrees(np.arctan(yMean / xMean))
angle = np.mean(angles)
print(angle)

rotMat = mathlib.gen_rotation_matrix(90-angle)

#print(rotMat)

xst = np.transpose(xs2 - xMean)
yst = np.transpose(ys2 - yMean)

xyst = np.stack((xst, yst))
#print(xyst)

#print(" ")

ans = np.matmul(rotMat, xyst)
#print(ans)

plt.subplot(1,2,1)
plt.scatter(ans[0], ans[1])
plt.yticks([-1, 0, 1, 2, 3])
plt.subplot(1,2,2)
plt.scatter(ans[0], ans[1])
plt.show()
