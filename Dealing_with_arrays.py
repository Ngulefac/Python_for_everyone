list = [1,2,3,4,5,6,7]
print(list) # prints out the whole array
print(list[0:3]) # prints out from index 0 to index 2 
print(list[2:])  # prints out from index 2 till the end of the list
print(list[:4]) #prints out from index 0 till the fourth element (index 3)
print(list[:])  #prints everything from the first index (index 0 till the last element)
#Rather than using 'print(list[:])' use 'print(list)' as they both do thesame thing with the later being the
#simplified one

# 2D arrays
nestlist = [1,2,[10,20,30,[7,9,11,[100,200,300]]],[1,7,8]]
print(nestlist[2][3]) #prints out the index 3 of the index 2 position in nestlist


