#The keyword argument syntax appends an equals sign after each variable name. If calling object does not provide this argument, then the default argument is used instead.

class Point:
    def __init__(self,x=0,y=0):
        self.move(x,y)

    def move(self, x, y):
        self.x=x
        self.y=y

    def reset(self):
        self.move(0,0)

p1=Point()
p2=Point(3,4)

print('p1.x=',p1.x,'p1.y=',p1.y)
print('p2.x=',p2.x,'p2.y=',p2.y)
