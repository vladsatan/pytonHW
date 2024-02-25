array = [1,2,3,4,5,6]

def change_order(arr):
    result = []

    k = round(len(arr)/2)

    for i in range(len(arr)):
        if(i < k):
            result.append(arr[i])
        else: break

    for i in range(len(arr)-1,-1,-1):
        if(i >= k):
            result.insert(0, arr[i])
        else: break

    return result;

array1 = [1,2,3,4,5,6]
array2 = [1,2,3,4,5,6,7,8,9,10]

change_order1 = change_order(array1)
change_order2 = change_order(array2)
    
print(change_order1)
print(change_order2)

