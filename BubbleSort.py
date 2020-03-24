def bubble_sort(lst):
    num_comparisons = len(lst) # ensures that numbers aren't unnecessarily compared
    for i in range(len(lst) - 1):  # makes number of passes n-1 (max number of passes required to sort)
        num_comparisons -= 1
        num_changes = 0
        for j in range(num_comparisons):  # loop for each pass
            temp = lst[j]
            if temp > lst[j + 1]: # compares values at index n and index n + 1
                lst[j] = lst[j + 1]
                lst[j + 1] = temp
                num_changes += 1
        if num_changes == 0:
            break
    return lst


print(bubble_sort([9,8,7,6,5,4,3,2,1]))
