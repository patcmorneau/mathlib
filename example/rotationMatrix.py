import sys, os
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__), 
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

from mathlib import mathlib
import numpy as np

print(mathlib.gen_rotation_matrix(90))
