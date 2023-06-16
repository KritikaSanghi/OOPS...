#variables: 
class car:
    wheel = 4 #class variale
    door = 5
    def __init__(self, color, model, maker):
        self.color = color #instance variable
        self.maker= maker
        self.model= model
car1 = car('red','ciaz','maruti')
print(car1.maker)  #calling instance var through obj
print(car.wheel)   #calling class var through class
print(car1.wheel)  #calling class var through obj
print(car.color)   #calling instance var through class: !error!
