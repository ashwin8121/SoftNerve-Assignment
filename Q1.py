# Question 1 : Leader in the Array
N = int(input()) # number of elements in the array / list
lst = []
for _ in range(N):
   inp = int(input()) # get elements of the array or the list
   lst.append(inp)

maxElement = -9999
for element in lst[-1::-1]:
    if element > maxElement:
        print(element, end=" ")
        maxElement = element
