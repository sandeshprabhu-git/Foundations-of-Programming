"""
Given a non-empty array, return true if there is a place to split the array so that the sum of the numbers on one side is equal to the sum of the numbers on the other side.


canBalance([1, 1, 1, 2, 1]) → true
canBalance([2, 1, 1, 2, 1]) → false
canBalance([10, 10]) → true

"""

def canBalance(nums):
    if len(nums) == 1:
        return False
    left, right = 0, 0
    n = len(nums)
    for i in nums:
        left += i
    for i in range(n-1, -1, -1):
        right += nums[i]
        left -= nums[i]
        if left == right:
            return True
    return False



print(canBalance([1, 1, 1, 2, 1]))
print(canBalance([2, 1, 1, 2, 1]))
print(canBalance([10, 10]))