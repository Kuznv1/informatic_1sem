'''class Node:
    def __init__(self, value): #конструктор (..,атрибут) def(аргумент) - функция
        self.value = value  # тело функции
        self.left = None
        self.right = None
        self.parent = None'''
from math import log, ceil

class Segment_Tree:
    def __init__(self, a):
        self.array = a
        k = 2**ceil((log(len(a), 2))) - len(a) # количество нулей в последней строчке
        # for i in range(k):
        #     self.array.append(0)
        self.array = [0] * (len(a) + k - 1) + self.array  + [0] * k  
        print(self.array)    
        for i in range(len(a) + k - 2, -1, -1):
            self.array[i] = self.array[2*i + 1] + self.array[2*i + 2]
        self.size = len(a)

    def sum(self):
        return self.array[0]
    
    def add(self, value):
        self.size += 1
        if 2**int(log(self.size, 2)) < self.size:
            i = self.size - 2 + 2**ceil(log(self.size, 2))
            self.array[i] = value
            while i >= 0:
                self.array[(i-1)//2] += value
                i = (i - 1) // 2

  

        
t = Segment_Tree([5, 24, 61])
print(t.array)
t.add(42)
print(t.array)

        
        
