# __author__ = 'Scott Businge'


class Car(object):
    def __init__(self, type='honda', model='GM', name='General'):  # instantiation
        self.moving_speed = self.moving_speed
        self.parked_speed = self.parked_speed
        self.moving_man = None
        self.num_of_doors = ''
        self.type = type
        self.model = model
        self.name = name

    def doors(self, num_of_doors):
        pass

    def drive(self, moving_man):
        return moving_man

    def wheels(self, num_of_wheels):
        return num_of_wheels

    def speed(self, parked_speed=0, movind_speed=0):
        return movind_speed
