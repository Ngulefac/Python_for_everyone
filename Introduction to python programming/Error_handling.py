
try:
   z = 1/56
except:
  print("That was silly!") #This is displayed if an error occurs in the try:
finally:   #Here you're saying that ,,,when the operation above is completed do this
  print("This gets executed no matter what")
  print(z)