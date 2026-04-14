def average(nums):
    total = 0
    for num in nums:
        total = total + num

    return total / len(nums)


nums = [1, 2, 3, 4]
print(average(nums))
