"""car class lab"""

class Car(object):
	def __init__(self, name='General', model='GM', car_type=''):
		self.car_type = car_type
		self.model = model
		self.name = name 
		self.num_of_doors = [4, 2, 2]

