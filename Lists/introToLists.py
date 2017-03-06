##this is just a simple list
#main purpose of this is just for me to go over the concepts of Lists in Py

movieSeries=['Harry Potter','Spider-Man','Batman','Hunger Games']

##to print
print(movieSeries)
##that printed the entire List

for items in movieSeries:
    print(items)
##that would print each item in the list, we can choose which one like
#movieSeries[i] to print a specific one

print(len(movieSeries))
##prints the length of the list

movieSeries.append("Adding a item to the back of the list")
print(movieSeries)

movieSeries.pop()
print(movieSeries)
##should have removed what was at the back of the list

movieSeries.remove("Batman")
print(movieSeries)
#removes Batman

movieSeries.insert(2,"Batman")
print(movieSeries)
#adds batman back to its original place, before list[2]
##Next Time i'll go over 2d arrays and hopefully move to dataStructures
##Check out my Java Code as Well
