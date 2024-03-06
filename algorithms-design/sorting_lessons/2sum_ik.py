# hash Table  Approach
# When you propose a solution always ask tradeoffs:
# Can I use extra memory? if yes then hash table is okay
# If not allow to use extra memory then use brute force


def twoSum(arr, sum):
    hashTable= {}
    for i in range(len(arr)):
        if arr[i] in hashTable:
            print(i,hashTable[arr[i]])
        hashTable[sum-arr[i]] = i
    
    print(hashTable)




# Check whether given key exist in python dictionary
# a = {1:0}
# 1 in a -> True
# 0 in a -> False




# arr = [5,3,1,9]
# sum = 6
# twoSum(arr, sum)



def twoSum(nums, target):
    hashtable = {"result":[]}
    result = []
    for index in range(len(nums)):
        value = target-nums[index]
        if value in hashtable:
            hashtable["result"].append(hashtable[value])
            hashtable["result"].append(index)
        hashtable[nums[index]] = index
    print(hashtable["result"])
    return hashtable

arr = [5,3,1,9]
sum = 6
print(twoSum(arr, sum))