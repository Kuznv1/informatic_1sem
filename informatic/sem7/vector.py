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
        else:
            return (self.x * other, self.y * other, self.z * other)
        
    def center_mass(self, other1, other2, other3, Masses):
        self.x = (other1.x * Masses[0] + other2.x * Masses[1] + other3.x * Masses[2])/sum(Masses)
        self.y = (other1.y * Masses[0] + other2.y * Masses[1] + other3.y * Masses[2])/sum(Masses)
        self.z = (other1.z * Masses[0] + other2.z * Masses[1] + other3.z * Masses[2])/sum(Masses)
        return self.x, self.y, self.z

    

a = Vector(1, 2, 3)
b = Vector(2, 4, 5)
'''print(a)
print(abs(a))
print(a + b)
#print(a + 1)
#print(1 + a)
#print(1 - b)
print(a * b)'''

P1 = Vector(1, 2, 3)
P2 = Vector(4, 5, 6)
P3 = Vector(0, 9, 2)

Mc = Vector(0, 0, 0)
M = [1, 2, 3]
#P = [x, y, z]
N_point = 3
#print(a*2)
print(Mc.center_mass(P1, P2, P3, M))