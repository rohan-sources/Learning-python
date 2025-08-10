class Item():
    def calc_price(self,x,y): # here. we give a parameter self, because when we call this method, it takes the 
                          #object itself as an argument. so to consider that, we give any parameter in the method header
                          #self is a name for that parameter by convention, any other can be used too
        return x*y
    
item1=Item() #called instance or object of the class Item
item1.name='Phone' # here name, price and quantity are attribukttes of the object item1
item1.price=100
item1.quantity=90
print(item1.calc_price(item1.price,item1.quantity)) # here item1 in the beginning is the self argument, and x,y the price and quantity ones

item2=Item() #called instance/object
item2.name='Laptop'
item2.price=1000
item2.quantity=3
print(item2.calc_price(item2.price,item2.quantity))

#here we see that every instance we define, we need to then input its name, price and quantity separately. this is annoying
#we can define it all while defining the instance using __init__ also called constructokr