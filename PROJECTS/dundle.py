class person:
    def __init__(self,name, address):
        self.name = name
        self.address = address
        
    def value(self):
#        print (f "my name is {}, I live is{}".format("self.name", "self.value"))
        print ("my name is:: " + self.name)

    
p1= person("rajan", "pokhara")    
    
print (p1.value())