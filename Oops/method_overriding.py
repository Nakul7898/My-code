class Shape:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def area(self):
        return self.x * self.y

class Circle(Shape):
    def __init__(self,redius,a,b):
        self.redius=redius
        super().__init__(a,b)

    def area(self):
        return self.redius * super().area()

a= Circle(4,1,2)
print(a.area())