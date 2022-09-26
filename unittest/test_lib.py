import sys, os
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__), 
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

from mathlib import mathlib
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
		self.assertTrue(inside)
		inside = mathlib.is_inside_rectangle(rect, point2)
		self.assertFalse(inside)
		inside = mathlib.is_inside_rectangle(rect, point3)
		self.assertFalse(inside)
		inside = mathlib.is_inside_rectangle(rect, point4)
		self.assertTrue(inside)
		
	def test_gen_matrix_rotation(self):
		vector = np.array([5,2])
		matrix_rotation = mathlib.gen_rotation_matrix(90)
		ans = matrix_rotation.dot(vector)
		ninetyDegreeRotationMatrix = np.array([[math.cos(math.radians(90)),-math.sin(math.radians(90))],[math.sin(math.radians(90)),math.cos(math.radians(90))]])
		ans2 = ninetyDegreeRotationMatrix.dot(vector)
		self.assertEqual(ans.all(), ans2.all())
		
		vector = np.array([5,2])
		matrix_rotation = mathlib.gen_rotation_matrix(35)
		ans = matrix_rotation.dot(vector)
		ninetyDegreeRotationMatrix = np.array([[math.cos(math.radians(35)),-math.sin(math.radians(35))],[math.sin(math.radians(35)),math.cos(math.radians(35))]])
		ans2 = ninetyDegreeRotationMatrix.dot(vector)
		self.assertEqual(ans.all(), ans2.all())
		
		vector = np.array([5,2])
		matrix_rotation = mathlib.gen_rotation_matrix(180)
		ans = matrix_rotation.dot(vector)
		ninetyDegreeRotationMatrix = np.array([[math.cos(math.radians(180)),-math.sin(math.radians(180))],[math.sin(math.radians(180)),math.cos(math.radians(180))]])
		ans2 = ninetyDegreeRotationMatrix.dot(vector)
		self.assertEqual(ans.all(), ans2.all())
		
		vector = np.array([5,2])
		matrix_rotation = mathlib.gen_rotation_matrix(270)
		ans = matrix_rotation.dot(vector)
		ninetyDegreeRotationMatrix = np.array([[math.cos(math.radians(270)),-math.sin(math.radians(270))],[math.sin(math.radians(270)),math.cos(math.radians(270))]])
		ans2 = ninetyDegreeRotationMatrix.dot(vector)
		self.assertEqual(ans.all(), ans2.all())
		
		vector = np.array([5,2])
		matrix_rotation = mathlib.gen_rotation_matrix(450)
		ans = matrix_rotation.dot(vector)
		ninetyDegreeRotationMatrix = np.array([[math.cos(math.radians(450)),-math.sin(math.radians(450))],[math.sin(math.radians(450)),math.cos(math.radians(450))]])
		ans2 = ninetyDegreeRotationMatrix.dot(vector)
		self.assertEqual(ans.all(), ans2.all())
		
	def test_unit_vector(self):
		v = np.array([5,20])
		u = mathlib.unit_vector(v)
		ans = math.sqrt(pow(u[0],2)+pow(u[1],2))
		self.assertEqual(1, ans)
		
		u2 = mathlib.unit_vector(np.array([0.2, 0.8]))
		self.assertEqual(u.all(), u2.all())

		
	def test_angle_between(self):
		angle = mathlib.angle_between(np.array([1,0]), np.array([0,1]))
		self.assertEqual(90, angle)
		
		angle = mathlib.angle_between(np.array([1,0]), np.array([math.sqrt(3)/2, 0.5]))
		self.assertEqual(30, round(angle))
		
		angle = mathlib.angle_between(np.array([1,0]), np.array([1, 1]))
		self.assertEqual(45, round(angle))
		
		angle = mathlib.angle_between(np.array([1,0]), np.array([-1, 0]))
		self.assertEqual(0, angle)
		
		angle = mathlib.angle_between(np.array([1,0]), np.array([0,-1]))
		self.assertEqual(90, angle)
		
		angle = mathlib.angle_between(np.array([1,0]), np.array([1,0]))
		self.assertEqual(0, angle)
		
		angle = mathlib.angle_between(np.array([1,0]), np.array([-math.sqrt(3)/2, 0.5]))
		self.assertEqual(30, angle)

	def test_angle_conversion(self):
		x = mathlib.angular2decimal("47°56’13’’")
		self.assertAlmostEqual(x, 47.937, 3)
		
		x = mathlib.decimal2angular(47.937)
		self.assertEqual(x, "47°56’13’’")
		
		
if __name__ == '__main__':
    unittest.main()
