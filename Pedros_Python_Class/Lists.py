
#List 
#Ordered sequence of values
# Mutable 

#Appending 
my_ls = [1,2,3,4]
my_ls.append(5)
print(my_ls)

#List Methods
#List Methods can be different Type such as: 
# L.append(e)
# L.extend(L1)
# L.insert(i,e)
# L.remove(e)
# L.pop(i)
# L.sort
# L.reverse

# Exercise 6: Use a list operation to create a list of ten elements, 
# each of which is '*'

juan_ls = []
juan_ls.extend(["*"]*10)
print(juan_ls)

#without list operation 

#juan_ls = ["*"] * 10

# Exercise 7: Assign each of the three elements in the list below to three variables a, b, c
ls = [['dogs', 'cows', 'rabbits', 'cats'], 'eat', {'meat', 'grass'}]

a = ls[0]
b = ls[1]
c = ls[2]

print(a)
print(b)
print(c)


# Exercise 8: Replace the last element in ls1 with ls2
ls1 = [0, 0, 0, 1]
ls2 = [1, 2, 3]




# Exercise 9: Create a new list that contains only unique elements from list x

x = [1, 5, 4, 5, 6, 2, 3, 2, 9, 9, 9, 0, 2, 5, 7]


# Exercise 10: Print the elements that occur both in list a and list b

a = ['red', 'orange', 'brown', 'blue', 'purple', 'green']
b = ['blue', 'cyan', 'green', 'pink', 'red', 'yellow']


# Exercise 11: Print the second smallest and the second largest numbers 
# in this list of unique numbers

x = [2, 5, 0.7, 0.2, 0.1, 6, 7, 3, 1, 0, 0.3]


# Exercise 12: Create a new list c that contains the elements of 
# list a and b. Watch out for aliasing - you need to avoid it here.

a = [1, 2, 3, 4, 5]
b = ['a', 'b', 'c', 'd']
