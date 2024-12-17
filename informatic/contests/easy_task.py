class Heap:     #max
    
    def __init__(self, a):
        self.array = a
        for i in range(len(self.array)//2, -1, -1):
            self.siftDown(i)
    
    def siftDown(self, i):
        while 2 * i + 1 < len(self.array):
            max_child_index = 2 * i + 1
            if 2 * i + 2 < len(self.array) and self.array[2 * i + 1] < self.array[2 * i + 2]:
                max_child_index = 2 * i + 2
            if self.array[i] > self.array[max_child_index]:
                break
            self.array[i], self.array[max_child_index] = self.array[max_child_index], self.array[i]
            i = max_child_index
        return
    
    def siftUp(self, i):
        while self.array[i] > self.array[(i - 1) // 2] and i > 0:
            self.array[i], self.array[(i - 1) // 2] = self.array[(i - 1) // 2], self.array[i]
            i = (i - 1) // 2
        return
    
    def add(self, value):
        self.array.append(value)
        self.siftUp(len(self.array) - 1)
    
    def pop(self):
        result = self.array[0]
        self.array[0] = self.array[-1]
        self.array.pop()
        self.siftDown(0)
        return result

n, k = list(map(int, input().split()))
h = Heap([])
m = 0
for element in list(map(int, input().split())):
    if m < k:
        h.add(element)
        m += 1 
        continue   
    if element < h.array[0]:
        h.add(element)
        h.pop()

def Quicksort(A):
    if len(A) == 1 or len(A) == 0:
        return A
    ref = A[len(A)//2]
    small = [number for number in A if number < ref]
    equal = [number for number in A if number == ref]
    big = [number for number in A if number > ref]
    return Quicksort(small) + equal + Quicksort(big)

h.array = Quicksort(h.array)
#h.array.sort()

'''def cocktail_sort(seq):
    n = len(seq)
    swapped = True
    start = 0
    end = n-1
    while swapped:
        swapped = False
        for i in range(start, end):
            if seq[i] > seq[i+1]:
                seq[i], seq[i+1] = seq[i+1], seq[i]
                swapped = True
        if not swapped:
            break
        swapped = False
        end -= 1
        for i in range(end-1, start-1, -1):
            if seq[i] > seq[i+1]:
                seq[i], seq[i+1] = seq[i+1], seq[i]
                swapped = True
        start += 1
    return(seq)'''
#h.array = cocktail_sort(h.array)
print(" ".join(map(str, h.array)))
