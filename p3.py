def find_max(numbers, compare):
    
    max_num = numbers[0]
    for num in numbers[1:]:
        max_num = compare(max_num, num)
    
    return max_num

numbers = [5, 3, 1, 6, 7, 8]

max_number = find_max(numbers, lambda x, y: x if x > y else y)
print(max_number)

