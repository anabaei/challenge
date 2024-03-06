######################### Execution ########################################
#########               python3 nameOfFile.py                         ######
#############################################################################

######################### Python Notes #####################################
#########  ########### ########### ###########  ###########   ###########                                                     
#########################################################################
# Execution 
# python3 nameOfFile.py

# range(0, len(arr))
# It starts from 0 to n-1 in length of n array


#reverse the best is 
#    for index in range(start,len(arr)):
#    i = len(arr)-index-1
#    print(i)

# For index in range(len(arr), 0, -1):
# in reverse order it starts from n to 1.  


################ Adding elements to an array ################
# INSERT: array.insert(index,value)  insert a specific index always
# Extend: it extends the current array with another array. array.extend(arr2)

# Append: Add one element to an array
# Append: Add the whole object into array, list inside list, array.append(arr2)

################################################################

# Convert array of string to array of chars
# for i in range(0, len(arr)):
#                 result.extend(arr[i])  


######################### Solutions #####################################
#########  ########### ########### ###########  ###########   ###########                                                     
#########################################################################

from multiprocessing.dummy import Array


class Solution:
    #BruteForce: Selection Sort
    #########################################################################
    def selectionArray(array):
        if len(array) <2:
            print(array(0))
            return 
        # min = {}
        # min[3]=0
        # min2 =(1,2)
        
        for index in range(0, len(array)):
            print("index =",index)
            for index2 in range(index, len(array)):
                print("index2 =",index2)
                if(array[index] > array[index2]):
                    #swap
                    temp = array[index]
                    array[index] = array[index2] 
                    array[index2] = temp

                # if(list(min.keys())[0]> item):
                #     min[item] = index 
                
            print(array)    
    # BruteForce Bubble Sort Min
    # n(n-1)/2 comparison
    #########################################################################
    def BubbleSort(arr):
        for i in range(0, len(arr)):
            for j in range(0, len(arr)-i-1):
                if(arr[j] > arr[j+1]):
                    temp = arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1] = temp

        print(arr)

    # BruteForce Bubble Sort: Sort from the end to the i+1
    #########################################################################
    def BubbleSortMax(arr):
        for index in range(len(arr)):
            for ind in range(index+1, len(arr)):
                index2 = len(arr) - ind 
                if(arr[index2] < arr[index2-1]):
                    temp = arr[index2-1]
                    arr[index2-1] = arr[index2]
                    arr[index2] = temp

        print(arr)


# BruteForce Insertion: 
# Insertion has two pointer:
# One regular travers the whole array i and starts from 1
# Another starts from 0, i-1 and always check all previeows values to the first
# to replace smallest value, 
# we have a key = a[i], because need to shift one to right, and duplicate a[j+1] = a[j]

#########################################################################

    def insert(arr):

        return arr

    def insertion(arr):
            for i in range(0, len(arr)):
                key = arr[i]
                j = i - 1
                while j>= 0 and key < arr[j]:
                    arr[j+1] = arr[j]
                    j = j-1 
                arr[j+1] = key
                # if( i == 0):
            print(arr) 



    def insertion_sort(arr):
        """
        Args:
        arr(list_int32)
        Returns:
        list_int32
        """
        for i in range(1, len(arr)):
            j = i-1 
            key = arr[i]
            while j >= 0 and  key < arr[j]:
                arr[j+1] = arr[j]
                j = j-1
            arr[j+1] = key 
        
        return arr


######################### Test ########################################
#########  ########### ########### ########### ########### ###########                                                         
#######################################################################
array = [3,2,4,32,1,0,4]
print(array)
array2 = ['Engineering', 'Medical']
# Solution.selectionArray(array)
#Solution.BubbleSortMax(array)
#Solution.insertion(array)
Solution.insertion_sort(array)