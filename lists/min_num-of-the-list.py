def min_numbers(nums):
    min_val=nums[0]
    
    for num in nums:
        if num<min_val:
            min_val=num

    return min_val


numbers=[3,4,8,9,2,36,17,1,22,5]
result=min_numbers(numbers)

print(f"The min of the list is {result}")
