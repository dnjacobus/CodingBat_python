def first_last6(nums):
    '''
    Given an array of ints, return True if 6 appears as either the first or last element in the array.
    '''
    return nums[0] == 6 or nums[-1] == 6

def same_first_last(nums):
    '''
    Given an array of ints, return True if the array is length 1 or more, 
    and the first element and the last element are equal.
    '''
    return len(nums) >= 1 and nums[0] == nums[-1]

def common_end(a, b):
    '''
    Given 2 arrays of ints, a and b, return True if they have the same first element 
    or they have the same last element.
    '''
    return a[0] == b[0] or a[-1] == b[-1]

def sum3(nums):
    '''
    Given an array of ints length 3, return the sum of all the elements.
    '''
    #return sum(nums)
    return nums[0] + nums[1] + nums[2]

def rotate_left3(nums):
    '''
    Given an array of ints length 3, return an array with the elements "rotated left".
    '''
    return [nums[1],nums[2],nums[0]]

def reverse3(nums):
    '''
    Given an array of ints length 3, return a new array with the elements in reverse order.
    '''
    return nums[::-1]

def max_end3(nums):
    '''
    Given an array of ints length 3, figure out which is larger, the first or last element in the array, 
    and set all the other elements to be that value. Return the changed array.
    '''
    max_num = max(nums[0],nums[2])
    nums[0] = max_num
    nums[1] = max_num
    nums[2] = max_num
    return nums

def sum2(nums):
    '''
    Given an array of ints, return the sum of the first 2 elements in the array. 
    If the array length is less than 2, just sum up the elements that exist.
    '''
    if len(nums) >=2:
        return nums[0] + nums[1]
    else:
        return sum(nums)

def middle_way(a, b):
    '''
    Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their middle elements.
    '''
    new_array = [a[1],b[1]]
    return new_array

def make_ends(nums):
    '''
    Given an array of ints, return a new array length 2 containing the first and last elements from the original array. 
    The original array will be length 1 or more.
    '''
    new_array = [nums[0],nums[-1]]
    return new_array

def has23(nums):
    '''
    Given an int array length 2, return True if it contains a 2 or a 3.
    '''
    return nums[0] == 2 or nums[0] == 3 or nums[1] == 2 or nums[1] == 3