# Python
# features
''' high-level DS - allows to express complex operations in a single statement
    simple but effective OOP
    elegant syntax, dynamic typing, interpreted nature, etc.
    makes it an ideal language for scripting and rapid application development
'''
""" we can write documentation or comments - for single line (one hash) and for a para like these two ways (three single quotation or three double quotation)
"""
import numbers


print("Meow!") #Meow!

x=10
print(x) #10
print(type(x)) #<class 'int'>
print(type(x).__name__) #int   double _ 
x="hello"
print(x) #hello  reassign possible for dynamic typing
print(type(x)) #<class 'str'>

#list
x=[1,'apple', 3.5, True]
print(x) #[1, 'apple', 3.5, True]  list can store different types of data but usually no need to do that
print(type(x)) #<class 'list'>

x1= ['a','b','c','d','e']
print(x1[4]) #e  
print(x1[-1]) #e minus index starts from the end of the list

#list slicing
#list_name[start : end : step]
print(x1[1:4]) #['b', 'c', 'd']  slicing-start index is inclusive, end index is exclusive
print(x1[:3])    # ['a', 'b', 'c'] index 0 to 2
print(x1[2:])    # ['c', 'd', 'e'] index 2 to 4
print(x1[:])    # full List
print(x1[::2])   # ['a', 'c', 'e'] index 0,2,4 bcz step =2
print(x1[::-1])  # ['e', 'd', 'c', 'b', 'a'] no start,end but step -1 so reverse

#list methods
numbers = [10, 20, 30]
numbers.append(40)
print(numbers) #[10, 20, 30, 40]
numbers.insert(1, 15) 
print(numbers) #[10, 15, 20, 30, 40] index 1, 15 insert
numbers.remove(20)
print(numbers) #[10, 15, 30, 40]
numbers.pop()
print(numbers) #[10, 15, 30]

#append vs extend
a = [1, 2]
a.append([3, 4])
print(a) #[1, 2, [3, 4]]  append adds the entire list as a single element

a = [1, 2]
a.extend([3, 4])
print(a) #[1, 2, 3, 4]  extend adds each element of the list as a separate element

#list comprehension
#baki ache

#tuple
numbers = (10, 20, 30, 40)
print(numbers) #(10, 20, 30, 40)
print(type(numbers)) #<class 'tuple'>
print(numbers[1]) #20
#numbers[1] = 25  #TypeError: 'tuple' object does not support item assignment  tuple is immutable
print(numbers.count(20)) #1  count of 20 in tuple
print (numbers.index(30)) #2  index of 30 in tuple

#list to tuple
l= [10, 20, 30]
t = tuple(l)
print(t) #(10, 20, 30)
#tuple to list
t= (10, 20, 30)
l = list(t)
print(l) #[10, 20, 30]  

#set
s = {10, 20, 30, 20, 40}
print(s)#{40, 10, 20, 30}  #set is unordered and unique elements
#list to set
l= [10, 20, 30, 20, 40]
s = set(l)
print(s)#{40, 10, 20, 30}  
s.add(50) 
s.update([60, 70]) 
print(s) #{70, 40, 10, 50, 20, 60, 30}  
s.remove(20) # if 20 not present then KeyError
s.discard(100) # if 100 not present then no error
print(s) #{70, 40, 10, 50, 60, 30}
#set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a | b) #{1, 2, 3, 4, 5, 6}   # Union
print(a & b) #{3, 4} # Intersection
print(a - b) #{1, 2} # Difference
print(a ^ b) #{1, 2, 5, 6} # Symmetric Difference
#membership test
print(3 in a)       # True
print(10 not in a)  # True
for x in a:
    print(x) 
#1 under 2 under 3 under 4 under

#dictionary
student = {
    "name": "Nirnita",
    "age": 23,
    "department": "CSE"
}

print(student) #
