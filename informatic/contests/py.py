def quick_sort1(nums):
    if len(nums) <= 1:
        return nums
    pivot = nums[0]
    left = [x for x in nums[1:] if x <= pivot]
    right = [x for x in nums[1:] if x > pivot]
    return quick_sort1(left) + [pivot] + quick_sort1(right)

words = input().split()

groups = {}
for word in words:
    sorted_word = ''.join(quick_sort1(list(word)))
    if sorted_word in groups:
        groups[sorted_word].append(word)
    else:
        groups[sorted_word] = [word]

# Сортировка групп: сначала по убыванию размера, потом по алфавиту
sorted_groups = sorted(groups.values(), key=lambda x: (-len(x), quick_sort1(x)))

for group in sorted_groups:
    print(" ".join(quick_sort1(group)))