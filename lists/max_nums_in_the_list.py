def max_numbers(nums):
    max_val=nums[0]

    for num in nums:
        if num > max_val:
            max_val=num

        return max_val
    
    numbers = [3,5,8,12,6,1,9]
    result = max_numbers(numbers)
    print(f"The maximum num in the list is {result}")
