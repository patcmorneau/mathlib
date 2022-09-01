import sys, os
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__), 
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

from mathlib import mathlib
import numpy as np

angle = mathlib.angle_between_abs(np.array([1,0]), np.array([0, -1]))
#print(angle)

angle = mathlib.angle_between(np.array([1,0]), np.array([0, -1]))
print(angle)
