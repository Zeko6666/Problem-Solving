from jovian.pythondsa import evaluate_test_cases
# I will make edge case :
test = {
    "input" : {
        "nums" : [1,3,5,6,7,8,9,10,11,13] , 
        "target" : 8
    },
    "output" : 5
}

tests = []
#  target occurs in middle :
tests.append(test)

# target occurs in the first :
tests.append({
    "input" :{
        "nums" : [1,3,5,6,7,8,9,10,11,13] , 
        "target" : 1
    },
    "output" : 0
})

# target occurs in the last :
tests.append({
    "input" : {
        "nums" : [9,10,11,13] , 
        "target" : 13
    },
    "output" : 3
})

# target occurs just one element in nums : 
tests.append({
    "input" :{
        "nums" : [1] , 
        "target" : 1
    },
    "output" : 0
})

# nums not contain target : 
tests.append({
    "input" : {
        "nums" : [13,11,10] , 
        "target" : 9
    },
    "output" : -1
})

# nums is empty : 
tests.append({
    "input" : {
        "nums" : [] , 
        "target" : 7
    },
    "output" : -1
})

# nums contains repeated numbers  :
tests.append({
    "input" :{
        "nums" : [0,1,1,1,1,10,11,13] , 
        "target" : 10
    },
    "output" : 5
})

#  nums contains multiple time of target :
tests.append({
    "input" :{
        "nums" : [ 0, 0, 0, 2, 2, 2, 3 , 6 , 6 , 6 , 6 , 6 , 6 , 8 , 8] , 
        "target" : 6
    },
    "output" : 7
})
def binary_search_algo(low, high,function):
    while low <= high : 
        mid = (low + high) // 2
        result = function(mid)
        if result == "found":
            return mid 
        elif result == "left" :
            high = mid - 1

        elif result == "right":
            low = mid + 1 
    return -1 

def location_target(nums,target):
    def function(mid):
        if nums[mid] == target:
            if mid - 1 >= 0  and nums[mid-1] == target :
                return "left"
            else:
                return "found"
        elif nums[mid] < target:
            return "right"
        else:
            return "left"
    return binary_search_algo(0,len(nums)-1 , function)

# print(location_target([-1,0,3,5,9,12],9))  # // 4 --> this is true value 

evaluate_test_cases(location_target,tests)