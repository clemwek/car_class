"""car class lab"""

class Car(object):
    def __init__(self, name='General', model='GM', car_type=''):
        self.car_type = car_type
        self.model = model
        self.name = name 
        self.num_of_doors = 2
        self.car_wheels = 4
        self.car_type = ''

        if self.name == 'Koenigsegg' or self.name == 'Porshe':
            self.num_of_doors = 2
        else: 
            self.num_of_doors = 4

        if self.vehicle_type=='trailer':
            self.num_of_wheels = 8
        else:
            self.num_of_wheels = 4

    try:
        def saloon(self):
            if self.vehicle_type == 'saloon':
                return True
            else:
                return False

        def drive(self, moving_speed):
            if moving_speed == 3:
                Car.speed = 1000
            elif moving_speed == 7:
                Car.speed = 77
            return self
    except Exception:
        return 'Error'



        

