
# inplace segregate odds/even numbers
# Two pointer from the last and first
class Solution:
    #BruteForce: Selection Sort
    #########################################################################
    def segregate(array):
        """
        Args:
        numbers(list_int32)
        Returns:
        list_int32
        """
        oi=0
        ei=len(array)-1
        while(oi < ei):
            while(array[oi]%2==0 ):
                oi +=1
            while(array[ei]%2==1 ):
                ei -=1
            print(oi, ei)
            if(oi > ei):
                return array
            print(array)
            temp = array[ei]
            array[ei] = array[oi]
            array[oi] = temp 
            oi +=1
            ei -=1
        print(array)
    
    ## using a fixed array with length of array
    def duth_flag(array):        
        start_index=0
        end_index=len(array)-1
        index=0
        result = ["G"] * len(array)
        start_index=0
        end_index=len(array)-1
        for i in range(0, len(array)):
            print(result)
            if(array[i]== "R"):
                result[start_index] =  "R"
                start_index +=1
            elif(array[i]== "B"):
                result[end_index] = "B"
                end_index -=1
        return result
    
    # better solution is to merge and make one then run it
    # better in place is using 3 pointers, 
    # one from the end of second array
    # one from the middle of second array
    # one from the last item in array on
    # then decrement, compare and put it into second array
    # at the end like merge sort add two loops to fill the rest
    # we may don't need the second loop since already in place if array one is exuast before array second

    def merge_one_into_another(first, second):
        result = []
        inf=0
        ins=0
        while(ins < len(second)):
            if(inf < len(first) and first[inf] <= second[ins]):
                result.append(first[inf])
                inf +=1
            elif(second[ins] ==0 and inf < len(first)):
                result.append(first[inf])
                inf +=1
            elif(second[ins] ==0):
                ins +=1
            else:
                result.append(second[ins])
                ins +=1
        
        print(result)


first= [2]
second= [1,0]
Solution.merge_one_into_another(first,second)

