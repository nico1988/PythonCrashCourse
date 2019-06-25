class Car():
    """模拟汽车"""
    def __init__(self, make, modle, year):
        self.make = make
        self.modle = modle
        self.year = year
        self.odometer_reading = 0
    def get_describe_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.modle
        return long_name.title()
    def read_odometer(self):
        """阅读里程表"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")
class ElectricCar(Car):
    def __init__(self,make, modle, year):
        super().__init__(make,modle,year)
        self.battery = Battery()
        # super(ElectricCar, self).__init__(make,modle,year) # python 2.7的写法
    def describe_battery(self):
        print("this car has a " + str(self.battery_size) + "-kwh battery.")

class Battery():
    def __init__(self, battery_size= 110):
        self.battery_size = battery_size
    def describe_battery(self):
        print("this car has a " + str(self.battery_size) + "-kwh battery.")
my_new_car = Car("audi",'a6',2018)
print(my_new_car.get_describe_name())
my_new_car.read_odometer()
my_new_car.odometer_reading = 121
my_new_car.read_odometer()

my_tesla = ElectricCar("tesla","modleS",2017)
print(my_tesla.get_describe_name())
my_tesla.odometer_reading = 9000
my_tesla.read_odometer()
my_tesla.battery_size = 117
my_tesla.describe_battery()
my_tesla.battery.describe_battery()