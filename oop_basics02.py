
class MyCircle:

    pi = 3.14

    def __int__(self, radius):

        self.radius = radius

    def get_circumference(self):

        return self.pi * self.radius * 2


# ###############################################################################
# class MathClass:
#
#     operations = 0
#
#     def __int__(self, a, b):
#
#         self.a = a
#         self.b = b
#
#     def add(self):
#
#         return self.a + self.b
#
#     def sub(self):
#
#         return self.a - self.b

###############################################################################
my_circle = MyCircle()
my_circle.radius = 15
print('pi value:', my_circle.pi)
print('radius:', my_circle.radius)

###############################################################################
# my_class = MathClass()
# my_class.a = 3
# my_class.b = 2
# print(my_class.a, my_class.b)
# print(my_class.add())
# print(my_class.sub())




