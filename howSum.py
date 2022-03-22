# This should return a path that sums to the targetNum
import re


def canSum(targetSum, numbers, memo, path):
    if targetSum == 0: # base case - exact amount reached, therefore return empty list
        return []
    if targetSum < 0: # base case - subtracted too much so that combo doesn't work
        return None
    
    if targetSum in memo: # 'base case' for memoization
        return memo[targetSum]

    for num in numbers:
        remainder = targetSum - num
        # if any of the child nodes return a list, there is a path to 0, so we should add what we subtracted
        if type(canSum(remainder, numbers, memo, path)) == list:
            memo[remainder] = path.append(num)
            return path
    
    #If we don't return True, we need to return False
    memo[targetSum] = None
    return memo[targetSum]


path = canSum(300, [7, 14], {}, [])
print(path)