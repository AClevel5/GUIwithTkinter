#positional arguments
# def add(*args):
#     sum_of_args = 0
#     for n in args:
#         sum_of_args += n
#     print(sum_of_args)
#
# add(1,2,5,6,7,8,9)

#Keyword arguments
# def calculate(**Kwargs):
#     for key, value in Kwargs.items():
#         print(key, value)
#
# calculate(add=3, multiply=5)

#Class with Key ward args. .get instead of brackets
class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")

my_car = Car(make="Porsche", model="GT3RS")

print(my_car.model)