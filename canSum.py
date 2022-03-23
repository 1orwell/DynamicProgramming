#This should check if we can sum some combination of numbers in the list to reach the target sum.
def canSum(targetSum, numbers, memo):
    if targetSum == 0: # base case - exact amount reached, therefore possible
        return True
    if targetSum < 0: # base case - subtracted too much so that combo doesn't work
        return False
    
    if targetSum in memo: # 'base case' for memoization
        return memo[targetSum]

    for num in numbers:
        remainder = targetSum - num
        # if any of the child nodes return true, there is a path to 0, so true
        if canSum(remainder, numbers, memo) == True:
            memo[remainder] = True
            return True
    
    #If we don't return True, we need to return False
    memo[targetSum] = False
    return False

boolean = canSum(300, [12, 10, 6, 5, 3, 4, 7], {})
print(boolean)