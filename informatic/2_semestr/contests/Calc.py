start, finish = map(int, input().split())
stop = 9999

def bfs(graph, start, znach):    
    visited = set()
    queue = []  

    queue.append(start)
    visited.add(start)

    while queue:
        node = queue.pop(0)
        
        if node == znach:    
            return 1            

        for neighboor in graph[node]:
            if neighboor not in visited:
                queue.append(neighboor)
                visited.add(neighboor)
    return 0




def Calc(start, finish):
    time = 0
    len_level = 1
    queue = []
    
    
    r = 1 #len_level 1
    r_r = 0

    if finish == 1:
        return start//2

    if finish < start:
        if finish < start//2:
            time = (start - start//2)//2
            start -= time*2
        queue.append(start)
        graph = {start:[]}
        while True:
            for n in range(r):
                now = queue.pop(0)
                
                value = now - 2
                if value < stop and value < start:
                    r_r += 1
                    graph[now].append(value)
                    graph[value] = []
                    queue.append(value)
                
                value = now * 3
                if value < stop and value < start: 
                    r_r += 1                   
                    graph[now].append(value)
                    graph[value] = []
                    queue.append(value)
                
                value = now + sum([int(i) for i in str(now)])
                if value < stop and  value < start:
                    r_r += 1
                    graph[now].append(value)
                    graph[value] = []
                    queue.append(value)
                #print(queue)
            r = r_r
            r_r = 0   

            time += 1  

            if finish in queue:
                return time

    else:
        queue.append(start)
        graph = {start:[]}
        while True:
            count = 0
            for n in range(len_level):
                now = queue.pop(0)
                value = now - 2
                if value > 0 and now != 0 and value not in graph:
                    graph[now].append(value)
                    graph[value] = []
                    queue.append(value)
                    count += 1
                
                value = now * 3
                if value < stop and value not in graph:
                    graph[now].append(value)
                    graph[value] = []
                    queue.append(value)
                    count += 1
                
                value = now + sum([int(i) for i in str(now)])
                if value < stop and value not in graph:
                    graph[now].append(value)
                    graph[value] = []
                    queue.append(value)
                    count += 1
            
            time += 1 # создали новый (time) уровень значений
            len_level = count

            if finish in queue:
                return time
        
print(Calc(start, finish))

        

        


        

        


