class Vector():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __abs__ (self):
        return ((self.x**2 + self.y**2 + self.z**2)**0.5)
    
    def __add__(self, other):
        if isinstance(other, Vector):
            return (self.x+other.x, self.y+other.y, self.z+other.z)
        elif isinstance(other, int) or isinstance(other, float):
            return Vector(self.x+other,self.y+other,self.z+other)

    def __radd__(self, other):
        assert isinstance(other, Vector), f'Сложение вектора и { type(other)}  невозможно'
        if isinstance(other, Vector):
            return (self.x+other.x,self.y+other.y,self.z+other.z)
    def __sub__(self, other):
        if isinstance(other, Vector):
            return (self.x-other.x, self.y - other.y, self.z - other.z) 
        elif isinstance(other, int) or isinstance(other, float):
            return Vector(self.x - other, self.y - other, self.z - other)

    def __rsub__(self, other):
        assert isinstance(other, Vector), f'Вычитание {type(other)} из вектора невозможно'
        
        if isinstance(other, Vector):
            return (self.x-other.x, self.y - other.y, self.z - other.z) 
        


    def __str__(self):
        return f'Вектор: x = {self.x} y = {self.y} z = {self.z}'
    
    def __mul__(self, other):
        if isinstance(other, Vector):
            return (self.x * other.x + self.y * other.y + self.z * other.z)
        
'''a = Vector(1, 2, 3)
b = Vector(2, 4, 5)
print(a)
print(abs(a))
print(a + b)
print(a + 1)
print(1 + a)
print(1 - b)
print(a * b)
'''
P1 = [1, 2, 3]
P2 = [4, 5, 6]
P3 = [4, 9, 2]
x = 1
y = 0
z = 0
P = [x, y, z]
N_point = 3



