#  i will solve it by linear_search_algorithm :

def linear_search_algo(arr,n):
    minimum_number = arr[0]
    index_minimum_number = 0 
    for i in range(n):
        if minimum_number > arr[i]:
            minimum_number = arr[i]
            index_minimum_number = i 
    return index_minimum_number

arr = [5, 6, 9, 0, 2, 3, 4]
n = 7
print(linear_search_algo(arr,n)) # // 3 times 

#  I will solve it by binary_search_algorithm :

def binary_search_algo(arr,n):
    low , high = 0 , len(arr)-1 
    if n % 2 == 0 :
        while low <= high:
            mid = (low + high) // 2 

            previous_value = (mid -1 +n) % n
            next_value = (mid+1) % n

            if arr[mid] <= arr[previous_value] and arr[mid] <= arr[next_value]:
                return mid 
            elif arr[mid] > arr[low]:
                high = mid -1 
            else :
                low = mid + 1
    else:
        while low <= high : 
            mid = (low + high) // 2 

            previous_value = (mid - 1 +n) % n  # to get value which before mid 
            next_value = (mid + 1) % n # to get value which after mid 

            if arr[mid] <= arr[previous_value] and arr[mid] <= arr[next_value]:
                return mid 
            elif arr[mid] < arr[low] :
                high = mid - 1 
            else:
                low = mid + 1

print(binary_search_algo(arr,n)) # // 3 times 