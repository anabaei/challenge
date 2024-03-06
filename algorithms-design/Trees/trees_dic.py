
################### Dictionary ############################
# Dictionary: A collection of n key, value pairs
# Given a key we can search for it and retrieve the value
# MAP and ASSOCIATED ARRAY are other names for dictionary

############################################################

# Implementing of Dictionary
    # 1- Contiguous Data structure like array
    # 2- Link DS like link list
    
    ###############  Array  (Contiguous Data structure) ######################
    # Operation  sorted               unsorted
    # Search     O(logn) use bsearch   O(n)
    # Insert     O(n) shift to right   O(1)
    # Delete     O(n) shift to left    O(n)
    #############################################
    
    # If keys are convenient integers smaller than m
    # Also if keys are string, we can convert them into unique numbers like mod of 14, 
    # then assign each value we call it Hash
    # Hash function does mapping from key to an interger index value

    # Unique keys from 0...n-1, 
    # Operation  indices
    # Search     O(1) 
    # Insert     O(1) 
    # Delete     O(1) 

    ################### Linked Data Structure ###############################
    # To avoid O(N), we can create a balance BST then 
    # Search     O(logn) 
    # Insert     O(logn) 
    # Delete     O(logn) 


    ############################# BST ##############################
    # BST is an implmentaion of dictionary
    # 