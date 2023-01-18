import random as rnd
import json
import const

test_size = const.test_size
input_size_max = const.input_size_max

# https://www.geeksforgeeks.org/python-program-for-subset-sum-problem-dp-25/

def isSubsetSum(set, n, sum) :
    
    # Base Cases
    if (sum == 0) :
        return True
    if (n == 0 and sum != 0) :
        return False
   
    # If last element is greater than
    # sum, then ignore it
    if (set[n - 1] > sum) :
        return isSubsetSum(set, n - 1, sum);
   
    # else, check if sum can be obtained
    # by any of the following
    # (a) including the last element
    # (b) excluding the last element   
    return isSubsetSum(set, n-1, sum) or isSubsetSum(set, n-1, sum-set[n-1])


def generateSusbsetSumInstance(lower_bound, upper_bound, input_size):
    a = []
    for i in range(input_size):
        a.append(rnd.randint(lower_bound,upper_bound))
    b = [a]
    b.append(rnd.randint(lower_bound,upper_bound))
    return b

test_cases = []
for i in range(2,input_size_max+1):
    for j in range(test_size):
        while (True):
            test_case = generateSusbsetSumInstance(1,20,i)
            if (not (isSubsetSum(test_case[0], len(test_case[0]), test_case[1]))):
                test_cases.append(test_case)
                break
        

with open(r'./test_data/test_cases.txt', 'w') as fp:
    json.dump(test_cases, fp)
       

with open(r'./test_data/test_cases.txt', 'r') as fp:
    basicList = json.load(fp)
print(basicList)