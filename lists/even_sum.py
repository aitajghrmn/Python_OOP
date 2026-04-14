def sum_even(nums):

    sum=0
    for num in nums :
        if num%2==0:
            sum+=num
    return sum

numbers=[1,2,3,4,5,6,7,8]
print(sum_even(numbers))
