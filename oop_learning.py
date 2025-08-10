class Item():
    discounted_price=0.8 #class attribute
    all_items=[]
    def __init__(self, name: str, price:float, quantity=0):  # here, we can specify that name has to be str. if we set it float, we can still give it an int. 
                                                            #when we give a default 0 in quantity which is an int, it is assumed that an int is expected and float is also accepted.
        # Validation of inputs
        assert price>=0, f'Price {price} is invalid.'
        assert quantity>=0, f'Price {quantity} is invalid.'

        # Assigning attributes to instance object
        self.name=name #here, we can make an attribute using init
        self.price=price
        self.quantity=quantity

        # Doing stuff needed as soon as instance is made
        Item.all_items.append(self)
    def calc_price(self): # here. we give a parameter self, because when we call this method, it takes the 
                          #object itself as an argument. so to consider that, we give any parameter in the method header
                          #self is a name for that parameter by convention, any other can be used too
        return self.price*self.quantity         # we don't need arguments for price and quantity, because we have defined it with init method
    def apply_discount(self):
        self.price*=self.discounted_price # Here, simply saying discounted_price won't work and you will have to mention its object, If instance is mentioned, attribute is searched at instance level first then class level.

    def __repr__(self):   # another magic method like __init__ to represent the coded version of the items as stored in all_items list
        return f'item(\'{self.name}\', {self.price}, {self.quantity})'    # by convention, we represent as in the instance's format
    
item1=Item('Phone',100,90.0) #called instance or object of the class Item
 # here name, price and quantity are attribukttes of the object item1
item1.calc_price() # here item1 in the beginning is the self argument, and x,y the price and quantity ones. but now, we have it all in the __init__ method

item2=Item('Laptop',1000,3) #called instance/object
item2.has_numpad=False

# here we see that every instance we define, we need to then input its name, price and quantity separately. this is annoying
# we can define it all while defining the instance using __init__ also called constructor for classes where there are always some attributes with an instance
# methods like __init__ are called magic methods
# when an instance is created in a class having __init__, python executes it automatically when the instance is defined
# for instance, here, inside the init method i said print i am created, so when the instance was defined, simulataneously, it printed i am created
# also, we can add other parameters in the init method header and use it to define the name, price and quantity in it itself

item3 = Item('Lamp', 500)
item3.discounted_price=0.5

# now, till now we saw only instance attributes. now, we will see class attributes. these belong to the class and can be applied to instances too.

Item.discounted_price # gives the discounted price of the whole class
item1.discounted_price # gives the discounted price of item1 only, same as all. item1 doesn't find this attribute in the instance level and then went to class level

dict_class=Item.__dict__ # gives all the attributes of the class at class level
dict_item=item2.__dict__ # gives all the attributes of the instance at its level

item1.apply_discount() #applies the 80% discount to item1

item3.apply_discount() #applies the 50% discount defined at instance level for item3

for i in Item.all_items:
    i.name # returns name of each item

print(Item.all_items)