def normalizing(arr):
    # arr is a list of length 11
    arr = list(int(value) for value in arr)

    max_value=[77, 1,4, 170, 371, 1,2,202, 1, 4, 3]
    min_value=[29,0,1,94,126,0,0,84.75,0,0,1]
    for i in range(0,11):
        if arr[i]>max_value[i]:
            arr[i]=max_value[i]
        if arr[i]<min_value[i]:
            arr[i]=min_value[i]
    ans=[0]*11
    for i in range(0,11):
        ans[i]=(arr[i]-min_value[i])/(max_value[i]-min_value[i])
    return tuple(ans)