import sys
sys.path.insert(0, '../')
import mathlib.mathlib as mathlib
import numpy as np
import math

import unittest

class TestLib(unittest.TestCase):
	def test_is_inside_rectangle(self):
		rect = (0,0,500,500)
		point = (100,100)
		point2 = (600,600)
		point3 = (500,501)
		point4 = (500,499)
		inside = mathlib.is_inside_rectangle(rect, point)
		assert inside
		inside = mathlib.is_inside_rectangle(rect, point2)
		assert not inside
		inside = mathlib.is_inside_rectangle(rect, point3)
		assert not inside
		inside = mathlib.is_inside_rectangle(rect, point4)
		assert inside
		
	def test_gen_matrix_rotation(self):
		vector = np.array([5,2])
		matrix_rotation = mathlib.gen_rotation_matrix(90)
		ans = matrix_rotation.dot(vector)
		ninetyDegreeRotationMatrix = np.array([[math.cos(math.radians(90)),-math.sin(math.radians(90))],[math.sin(math.radians(90)),math.cos(math.radians(90))]])
		ans2 = ninetyDegreeRotationMatrix.dot(vector)
		assert np,logical_and(ans,ans2)
		
		vector = np.array([5,2])
		matrix_rotation = mathlib.gen_rotation_matrix(35)
		ans = matrix_rotation.dot(vector)
		ninetyDegreeRotationMatrix = np.array([[math.cos(math.radians(35)),-math.sin(math.radians(35))],[math.sin(math.radians(35)),math.cos(math.radians(35))]])
		ans2 = ninetyDegreeRotationMatrix.dot(vector)
		assert np,logical_and(ans,ans2)
		
		vector = np.array([5,2])
		matrix_rotation = mathlib.gen_rotation_matrix(180)
		ans = matrix_rotation.dot(vector)
		ninetyDegreeRotationMatrix = np.array([[math.cos(math.radians(180)),-math.sin(math.radians(180))],[math.sin(math.radians(180)),math.cos(math.radians(180))]])
		ans2 = ninetyDegreeRotationMatrix.dot(vector)
		assert np,logical_and(ans,ans2)
		
		vector = np.array([5,2])
		matrix_rotation = mathlib.gen_rotation_matrix(270)
		ans = matrix_rotation.dot(vector)
		ninetyDegreeRotationMatrix = np.array([[math.cos(math.radians(270)),-math.sin(math.radians(270))],[math.sin(math.radians(270)),math.cos(math.radians(270))]])
		ans2 = ninetyDegreeRotationMatrix.dot(vector)
		assert np,logical_and(ans,ans2)
		
		vector = np.array([5,2])
		matrix_rotation = mathlib.gen_rotation_matrix(450)
		ans = matrix_rotation.dot(vector)
		ninetyDegreeRotationMatrix = np.array([[math.cos(math.radians(450)),-math.sin(math.radians(450))],[math.sin(math.radians(450)),math.cos(math.radians(450))]])
		ans2 = ninetyDegreeRotationMatrix.dot(vector)
		assert np,logical_and(ans,ans2)
		
		
		

if __name__ == '__main__':
    unittest.main()
