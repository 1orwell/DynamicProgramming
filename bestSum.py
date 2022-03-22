def bestSum(targetSum, numbers, memo):
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None
    
    #keep track of shortest list returned to this item
    shortest_path = None

    if targetSum in memo:
        return memo[targetSum]

    for num in numbers:
        remainder = targetSum - num
        possible_path = bestSum(remainder, numbers, memo)
        #returned a list so summation possible
        if type(possible_path) == list:
            possible_path.append(num)
            # compare to other paths to that node, is there one shorter?
            if shortest_path == None or len(possible_path) < len(shortest_path):
                shortest_path = possible_path
    
    memo[targetSum] = shortest_path
    return shortest_path

print(bestSum(8, [2, 4, 5], {}))