def max_sum(a,n):
    #code here
    if len(a) == 0:
        return 0
    
    sumA = sum(a)
    sumElement = 0
    for i,tmp in enumerate(a):
        sumElement += i*tmp
        
    sumK = sumElement
    result = sumElement
    for i in range(1,n):
        sumK =sumK + sumA - (n * a[n-i])
        result = max(result, sumK)
        
    return result
    