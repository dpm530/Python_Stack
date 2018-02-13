class Bike(object):
    def __init__(self,price,max_speed,miles=0):
        self.price=price
        self.max_speed=max_speed
        self.miles=0
    def displayinfo(self):
        print self.price
        print self.max_speed
        print self.miles
    def ride(self):
        print "Riding"
        self.miles+=10
    def reverse(self):
        print "Reverse"
        if self.miles>=5:
            self.miles-=5

bike1=Bike(200,"25 mph")
bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.displayinfo()

bike1=Bike(200,"25 mph")
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.reverse()
bike1.displayinfo()

bike1=Bike(200,"25 mph")
bike1.reverse()
bike1.reverse()
bike1.reverse()
bike1.displayinfo()
