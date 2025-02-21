def bin_search(element, List):
    index_mid = len(List)//2 
    value_mid = List[index_mid]
    
    new_list = List.copy()
    a = 0
    while len(new_list) > 1  :        
        if value_mid == element:
            a = 1
            return List.index(value_mid)            
        
        elif value_mid < element:
            new_list = new_list[index_mid:]
            index_mid = len(new_list)//2
            value_mid = new_list[index_mid]
        
        else:
            new_list = new_list[:index_mid]
            index_mid = len(new_list)//2
            value_mid = new_list[index_mid]
    if a == 0:
        return None


A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(bin_search(7, A))
print(bin_search(11, A))