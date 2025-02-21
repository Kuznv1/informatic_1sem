A = [9, 4, 8, 7, 2, 3, 1]

L1 = len(A)
for m in range(L1):                                  #сортируем массив значений
    for n in range(0, L1 - m - 1):
        if int(A[n]) > int(A[n + 1]):
            A[n], A[n + 1] = A[n + 1], A[n]

print(A)

def insertion_sort(nums):    #сортировка вставками
    # Сортировку начинаем со второго элемента, т.к. считается, что первый элемент уже отсортирован
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        # Сохраняем ссылку на индекс предыдущего элемента
        j = i - 1
        # Элементы отсортированного сегмента перемещаем вперёд, если они больше
        # элемента для вставки
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        # Вставляем элемент
        nums[j + 1] = item_to_insert

# Проверяем, что оно работает
random_list_of_nums = [9, 1, 15, 28, 6]  
insertion_sort(random_list_of_nums)  
print(random_list_of_nums)

#сортировка выбором
def selection_sort(nums):  
    # Значение i соответствует кол-ву отсортированных значений
    for i in range(len(nums)):
        # Исходно считаем наименьшим первый элемент
        lowest_value_index = i
        # Этот цикл перебирает несортированные элементы
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        # Самый маленький элемент меняем с первым в списке
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]

# Проверяем, что оно работает
random_list_of_nums = [12, 8, 3, 20, 11]  
selection_sort(random_list_of_nums)  
print(random_list_of_nums)

'''def select_sort(A):
    for i in range(len(A) - 1):
        min_index = i
        for k in range(i + 1, len(A)):
            if A[k] < A[min_index]:
                A[k], A[min_index] = A[min_index], A[k]
    return A'''