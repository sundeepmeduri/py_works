class Car:

    # class object attributes and same for all instance of class
    seats = 4

    def __init__(self, make, model, year, is_hybrid):

        # create attributes and assign using self.
        self.make = make
        self.model = model
        self.year = year

        # expected to be boolean
        self.is_hybrid = is_hybrid

    def desc(self):

        print('Car make is {0}, model is {1} and manufactured in year {2} and has {3} seats'.format(self.make, self.model, self.year, self.seats))



###########################################################################
# my_car = Car('honda', 'crv')  # we can create either way
my_car = Car(make='honda', model='crv', year=2018, is_hybrid=False)  # object is created
# print(type(my_car))
print(my_car.make)
print(my_car.model)
print(my_car.year)
is_hybrid = 'Yes' if my_car.is_hybrid is True else 'No'
print(is_hybrid)
print(my_car.seats)
my_car.desc()


print('\n--- car 2')
my_car2 = Car(year=2020, make='range rover', model='sport', is_hybrid=True)  # object is created
my_car2.seats = 6
# print(type(my_car))
print(my_car2.make)
print(my_car2.model)
print(my_car2.year)
is_hybrid = 'Yes' if my_car2.is_hybrid is True else 'No'
print(is_hybrid)
print(my_car2.seats)
my_car2.desc()
#################################################################################

