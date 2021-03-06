#oh my gosh, it worked
def gridTraveler(m,n,memo):
    if m == 1 and n == 1:
        return 1
    if m==0 or n == 0:
        return 0
    elif (m,n) in memo:
        return memo[(m,n)]
    #number of paths will be the same, just rotated grid by 90 degrees
    elif (n,m) in memo:
        return memo[(n,m)]
    else:
        memo[(m,n)] = gridTraveler(m-1,n,memo) + gridTraveler(m,n-1,memo)
    return memo[m,n]

options = gridTraveler(6,6,{})
print(options)

options = gridTraveler(60,100,{})
print(options)

options = gridTraveler(1,1,{})
print(options)