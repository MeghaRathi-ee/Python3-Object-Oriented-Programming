# Add an initialization method on point class that requires the user to supply x and y coordinates when the point object is instantiated

class Point:

    def __init__(self,x,y):
        self.move(x,y)
    
    def move(self,x,y):
        self.x=x
        self.y=y
        
    def reset(self):
         self.move(0,0)

point = Point(3, 5)
print(point.x,point.y)
        
