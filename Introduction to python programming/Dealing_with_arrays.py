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
print(nestlist[2][3][0]) #prints out the index 0 of index 3 of the index 2 position in nestlist
# in other words 
# print(nestlist[2][3][0]) means
# get the index 2 element,inside index 2 get the index 3 element, inside index 3 get the first element ,index 0
# print it out

t = ("23", "abc", "4.56", "2,3", "def" , "wow","this", "is", "great.")
print(t[2])
print(t[-5]) # Prints the last 5th element from the end(or extreme)

print(t[-4:]) # Prints the last 4th element till the last from the end(or extreme)

