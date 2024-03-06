
######################### Python Notes #####################################
#########  ########### ########### ###########  ###########   ###########                                                     
#########################################################################

### Sort an Array ####
# 1 - Brute force but n2 is not good 
# 2 - Merge, Quick, Heap sort nlogn
######################
# Down part of merge sort is space n
# Benefit is nlogn is gurantee 

# quick sort space memory is constant but the recursion takes memory
# heap sort has a constant space memory, cash behvior is not great and it is not sable

###
# Inputs: 
# if array of integers, stability is not important. 
# if array of objects, then we need to consider. 
# - A stable sorting algorithm maintains the relative order of the items with equal sort keys.


# execute python with self params
# Solution().func(arr)
# func(self,arr) --> func should be like this

# call a function itself
# self.func(self,arr) when you define it as 
# func(self,arr)

# split arr from an index
# arr[:3] -> includes 0,1,2 indexes
# arr[3:] -> includes 3,4,5,.. indexes

# Log in most cases here is log based on 2 and not 10. 
# 2^logn = n
# Big Omega n means lower bound of n
# teta n means a constant propotion of n like cn
# O, big Oh notation is upper bound means worst case scenario

############# Merge Sort ###########

class Solution:
    def mergeSort(self, arr):
        
        result = []
        if(len(arr)>1):
            pivot = len(arr)//2
            left = arr[:pivot]
            right = arr[pivot:]
            
            self.mergeSort(left)
            self.mergeSort(right)
        
            
            i = j = k = 0
            while(i < len(left)  and j < len(right) ):
                
                if left[i] <= right[j]:
                    arr[k] = left[i]
                    i +=1
                else:    
                #it came here when i = 3 when len of arr is 2, so use else if(left[i] > right[j]):
                    arr[k] =right[j]
                    j +=1
                k +=1
                
            while(j < len(right)):
                arr[k] =right[j]
                j +=1
                k +=1

            while(i < len(left)):
                arr[k] =left[i]
                i +=1
                k +=1

        print(arr)


arr =[32,2,3,5,22,33,21,7,6]
Solution().mergeSort(arr)

