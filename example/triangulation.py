import sys, os
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__), 
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)
print(sys.path)
from mathlib import mathlib
import numpy as np
import cv2 as cv

points = [(100,100),(200,500),(300,700),(400,400),(400,900),(500,100),(600,600),(700,300),(800,500),(900,100)]

triangles = mathlib.triangulate(points)

img = np.zeros(shape=[900, 900, 3], dtype=np.uint8)

for t in triangles:
	pt1 = (int(t[0]), int(t[1]))
	pt2 = (int(t[2]), int(t[3]))
	pt3 = (int(t[4]), int(t[5]))

	cv.line(img, pt1, pt2, (255,255,255), 1, cv.LINE_AA, 0)
	cv.line(img, pt2, pt3, (255,255,255), 1, cv.LINE_AA, 0)
	cv.line(img, pt3, pt1, (255,255,255), 1, cv.LINE_AA, 0)

cv.imshow("Result", img)
cv.waitKey(0)
cv.destroyAllWindows()

