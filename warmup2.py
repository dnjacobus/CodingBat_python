def string_times(string, n):
    '''
    Given a string and a non-negative int n, 
    return a larger string that is n copies of the original string.
    '''
    return string *n

def front_times(string, n):
    '''
    Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, 
    or whatever is there if the string is less than length 3. 
    Return n copies of the front;
    '''
    if len(string) <= 3:
        return string*n
    return string[:3]*n

def string_bits(string):
    '''
    Given a string, return a new string made of every other char starting with the first, 
    so "Hello" yields "Hlo".
    This is my solution. 
    '''
    new_str = []
    for i in range(len(string)):
        if i % 2 == 0:
            new_str.append(string[i])
    return ''.join(new_str)

#I like the solution that was given, it is a little cleaner
#Not my solution, its the solution given
def string_bits(string):
    result = ""
    for i in range(len(string)):
        if i % 2 == 0:
            result += string[i]
    return result

def string_splosion(str):
    '''
    Given a non-empty string like "Code" return a string like "CCoCodCode".
    '''
    result = ''
    for i in range(len(string)):
        part = string[:i+1]
        result += part
    return result

def last2(str):
    '''
    Given a string, return the count of the number of times that a substring length 2 appears in the string
    and also as the last 2 chars of the string, 
    so "hixxxhi" yields 1 (we won't count the end substring).
    '''
    end = str[-2:]
    subs = []
    for i in range(len(str[:-2])):
        if str[i:i+2] == end:
            subs.append(str[i:i+2])
    return len(subs)

#last2 was tricky. I got it correct, but its better to use a count instead of len(list)
#the function below was the given solution with a counter. A trick I need to practice
def last2(str):
    # Screen out too-short string case.
    if len(str) < 2:
        return 0
  
    # last 2 chars, can be written as str[-2:]
    last2 = str[len(str)-2:]
    count = 0
  
    # Check each substring length 2 starting at i
    for i in range(len(str)-2):
        sub = str[i:i+2]
        if sub == last2:
            count += 1
    return count 

def array_count9(nums):
    '''
    Given an array of ints, return the number of 9's in the array.
    '''
    count = 0
    for i in range(len(nums)):
        if nums[i] == 9:
            count += 1
    return count

#I did too much, can use a standard loop b/c its not a string
#Below is solution code

def array_count9(nums):
    count = 0
    for num in nums:
        if num == 9:
            count = count + 1

    return count

def array_front9(nums):
    '''
    Given an array of ints, return True if one of the first 4 elements in the array is a 9. 
    The array length may be less than 4.
    '''
    return 9 in nums[:4]

def array123(nums):
    '''
    Given an array of ints, return True if the sequence of 
    numbers 1, 2, 3 appears in the array somewhere.
    '''
    match_list = [1,2,3]
    for i in range(len(nums)):
        if nums[i:i+3] == match_list:
        return True
    return False