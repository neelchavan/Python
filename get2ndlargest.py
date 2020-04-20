#Unsorted list with duplicates
numbers = [3,4,2,4,6,6]
#removing duplicates
numbers = list(dict.fromkeys(numbers))
#sort the list
numbers.sort()
#remove first max number
numbers.remove(max(numbers))
#then print second highest number as the first highest
print(max(numbers))
