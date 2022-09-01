def linear_search_algo(nums , target):
    position = 0 
    while position <= len(nums) -1 :
        if nums[position] == target:
            return position
        else:
            position += 1 
    return -1 

print(linear_search_algo([13,11,10,9,8,7,6,5,3,1] , 5)) # // 7 