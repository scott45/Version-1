__author__ = 'Scott Businge'

class Andela(object):

    def __init__(self, country, city, ):
        self.country = country
        self.city = city


class Andelan(Andela):

    def __init__(self, country, city, first, last, role, pay ):
        super().__init__(country, city)
        self.first = first
        self.last = last
        self.role = role
        self.pay = pay




class Fellow(Andela):
    pass


class Bootcamper(Andela):
    pass
