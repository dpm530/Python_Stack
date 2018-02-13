class Products(object):
    def __init__(self,price,item_name,weight,brand,cost,status="for sale"):
        self.price=price
        self.item_name=item_name
        self.weight=weight
        self.brand=brand
        self.cost=cost
        self.status="for sale"

    def sell(self):
        self.status="sold"
        return self
    def add_tax(self):
        tax=.07
        return self.price *(1+tax)

    def return_item(self,reason):
        self.reason=reason
        if reason=="defective":
            self.status="defective"
            self.price=0
        elif reseon=="none":
            self.status="for sale"
        elif reason=="open box":
            self.status="used"
            self.price*=0.80

        return self
    def displayinfo(self):
        print "Price: " + str(self.price)
        print "Item Name: " + str(self.item_name)
        print "Weight: " + str(self.weight)
        print "Brand: " + str(self.brand)
        print "Cost: " + str(self.cost)
        print "Status: " + str(self.status)
        return self



product1=Products(10,"Cereal",0.5,"Special K",10)
product1.displayinfo()
product2=Products(20,"Pizza",0.2,"Pizza Hut",20)
product2.displayinfo()
