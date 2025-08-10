class Item():
    def __init__(self, name: str, price:float, quantity=0):  # here, we can specify that name has to be str. if we set it float, we can still give it an int. when we give a default 0 in quantity which is an int, it is assumed that an int is expected and float is also accepted.
        self.name=name #here, we can make an attribute using init
        self.price=price
        self.quantity=quantity
    def calc_price(self): # here. we give a parameter self, because when we call this method, it takes the 
                          #object itself as an argument. so to consider that, we give any parameter in the method header
                          #self is a name for that parameter by convention, any other can be used too
        return self.price*self.quantity         # we don't need arguments for price and quantity, because we have defined it with init method
    
item1=Item('Phone',100,90.0) #called instance or object of the class Item
 # here name, price and quantity are attribukttes of the object item1
print(item1.calc_price()) # here item1 in the beginning is the self argument, and x,y the price and quantity ones

item2=Item('Laptop',1000,3) #called instance/object
item2.has_numpad=False
print(item2.calc_price())

# here we see that every instance we define, we need to then input its name, price and quantity separately. this is annoying
# we can define it all while defining the instance using __init__ also called constructor for classes where there are always some attributes with an instance
# methods like __init__ are called magic methods
# when an instance is created in a class having __init__, python executes it automatically when the instance is defined
# for instance, here, inside the init method i said print i am created, so when the instance was defined, simulataneously, it printed i am created
# also, we can add other parameters in the init method header and use it to define the name, price and quantity in it itself

item3 = Item('Lamp', 500)