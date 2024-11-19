class Rectangle:
    def __init__(self, length, width): # constructor 
        self.length = length
        self.width = width 
        
    def area(self): #class function 
        return self.length * self.width 
        
    def perimeter(self):
        return 2 * self.length + 2 * self.width                 
    
    

length = int(input("Enter length: "))
width = int(input("Enter width: "))
Rec = Rectangle(length, width)
print("area:", r.area())
print("perimeter:", r.perimeter())

input()