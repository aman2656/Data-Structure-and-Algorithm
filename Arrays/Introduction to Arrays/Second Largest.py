def second_largest(arr,n):
    ans = None
    # YOUR CODE GOES HERE
    if len(arr) == 1:
        return -1
    ma = arr[0]
    index = 0
    se = arr[0]
    for i in range(1, len(arr)):
        if arr[i]>ma:
            ma = arr[i]
            index = i
    for j in range(0, len(arr)):
        if arr[j] <= ma:
            if j!=index:
                if arr[j] > se:
                    se = arr[j]
    return se
        

    
    
    return ans
