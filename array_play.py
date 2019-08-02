
'''
Write a function that takes two unsorted lists and returns a merged sorted list
A = [10, 8, 50, 40, 100, 89, 90]    
B = [2, 1, 44, 40, 88, 91, 77, 11, 22, 20, 99, 92]
c = []

'''
# Sort one of the lists sort()

sorted_list =  A.sort():

# Determine the location for one item in the next list 
# A = [2,3]
# B = [1,9,4,7]
def find_location(sorted_list, B):
    c = []
    for b_element in B:
        #9
        i = 0
        for a_element in sorted_list:
            if b_element > a_element:
                continue
            else #b_element <= a_element
                sorted_list.insert(i, b_element)
            i+=1
    c = sorted_list
    return c
            
        
# nested lesser greater
# Insert that item .append
# repeat for rest of the list - for 
# return C 

# OR, the simple way:
# c = a+b
# sort(c)
    
# for loop 


        
def say_hello():
    print('Hello, Ashish')

for i in range(5):
    say_hello()
