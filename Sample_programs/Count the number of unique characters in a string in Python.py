# Python program for the above approach 
  
# Function to count the number of distinct 
# characters present in the string str 
def countDis(str): 
  
    # Stores all distinct characters 
    s = set(str) 
  
    # Return the size of the set 
    return len(s) 
  
  
# Driver Code 
if __name__ == "__main__": 
  
    # Given string S 
    S = "SWIFTechnologies"
  
    print(countDis(S)) 
