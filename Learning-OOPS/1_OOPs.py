class Car:
    
    total_car = 0
    
    def __init__(self, brand, name):
        self.__brand = brand
        self.__name = name
        Car.total_car += 1
    
    def full_name(self):
        return (f"{self.__brand} {self.__name}") 
    
    def get_brand(self):
        return self.__brand + "!!!"
    
    def fuel_type(self):
        return "Petrol or Disel"
    
    @staticmethod
    def general_description():
        return " Cars are means of Transpotation"
    
    @property
    def model(self):
        return self.__name
    
class Electric_Car(Car):
    def __init__(self, brand, name, battery_size):
        super().__init__(brand, name)
        self.battery_size = battery_size
    def fuel_type(self):
        return "Electric Charge"  
    
class Battery:
    def battery_info(self):
        return "This  battery  contains 100kwh worth of power"

class Engine:
    def engine_info(self):
        return "This Engine is of 200CC and is a v12 engine "

class ElectricCartwo(Battery, Engine, Car):
    pass

my_tesla = Electric_Car("Tesla", "Model S", "85 kwh")

print(f"Is 'my_tesla' is an Instance of Car class :{isinstance(my_tesla, Car)}")
print(f"Is 'my_tesla' is an Instance of Electric_Car class: {isinstance(my_tesla, Electric_Car)}")


# print(f"Car Brand is : {my_tesla.brand}")
# print(f"Full Name: {my_tesla.full_name()}")
# print(my_tesla.get_brand())

print(f"Fule Type of Tesla is : {my_tesla.fuel_type()}")

my_car = Car("Tata", "Safari")
nexon = Car("Tata", "Nexon")
# print(f"Fule type of Safari is: {safari.fuel_type()}")
# print(f"Genetal Description of  car is :  {my_car.general_description()}")
# print(f"Genetal Description of  car is :  {Car.general_description()}")
# print(f"Total Car class has been called here is:  {Car.total_car}")
# my_car.model = "City"
print(f"After overwriting the name i want to see we can overwrite the private variable or not : {my_car.model} ")
    
# my_car = Car("BMW", "M3")
# print(f"Car Brand: {my_car.brand}")
# print(f"Car Name: {my_car.name}")
# print(f"Full Car Name: {my_car.full_name()}")



# my_new_car = Car("Audi", "A4")
# print(f"Car Brand: {my_new_car.brand}")
# print(f"Car Name: {my_new_car.name}")

my_new_tesla = ElectricCartwo("Tesla", "Model S")
print(f"Checking if we can access the battery class through multipel inheritance: {my_new_tesla.battery_info()}")
print(f"Checking if we can access the engine class through multipel inheritance: {my_new_tesla.engine_info()}")
