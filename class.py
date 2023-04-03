class Car:
    def __init__():
        
        self.model = "S600"
        self.color = "Red" # ends up on the object
        self.make = "Mercedes" # becomes a local variable in the constructor

car = Car()

print(car.color) # "Red"
print(car.make) # would result in an error, `make` does not exist on the object
#Let us sort that out. by self.make.
