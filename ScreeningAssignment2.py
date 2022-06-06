#2. Demonstrate use of abstract class, multiple inheritance and decorator in
#python using examples.

# Example for abstract class
from abc import ABC, abstractmethod
class Shape:
    def __init__(self,type):
        self.type=type


    @abstractmethod
    def Area(self):
        pass

    def getShapeType(self):
        return self.type

class Rectangle(Shape):
    def __init__(self,type,length,breadth):
        super().__init__(type)
        self.length=float(length)
        self.breadth=float(breadth)
    #implementing abstract method Area from Shape
    def Area(self):
        return self.length*self.breadth


class Triangle:
    def __init__(self,angle):
        self.angle=angle

    def getAngle(self):
        return self.angle

    def getTriangleProperties(self):
        return "A triangle has 3 sides and 3 angles"

#Multiple inheritance - inherits from both Triangle and Shape
class EquilateralTriangle(Triangle,Shape):
    def __init__(self,type,angle=60,side=1,):
        Triangle.__init__(self,angle)
        Shape.__init__(self,type)
        self.side=side
    def Area(self):
        return (0.43301)*(self.side**2)



#Decorator Example
import time

def defineFunctionStartAndEnd(funct):
    def calc(*args,**kwargs):
        time1=time.time()
        print(f'Start time of function:{time1}')
        funct(*args,**kwargs)
        time2=time.time()
        print(f'End time of function:{time2}')

        print(f'Total time taken {time2-time1} sec')
    return calc

@defineFunctionStartAndEnd
def bigCalculation(sleepTime):
    time.sleep(sleepTime)
    print('Done')

bigCalculation(6)



