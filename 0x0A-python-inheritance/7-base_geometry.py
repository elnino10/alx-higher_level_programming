#!/usr/bin/python3
"""BaseGeometry class"""


class BaseGeometry:
	"""BaseGeometry class"""
	def area(self):
		raise Exception('area() is not implemented')

	def integer_validator(self, name, value):
		"""validates value as an integer"""
		if not isinstance(value, int):
			raise TypeError(f"{name} must be an integer")
		if value <= 0:
			raise ValueError(f"{name} must be greater than 0")
