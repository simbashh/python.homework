Level1
1
companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print(len(companies))
#2
companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
companies.add("Twitter")
print(companies)
#3
companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
a=input("What elemant do you want to add ?  ")
a_list=a.split(" ")
companies.update(a_list)
print(companies)
#4
companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
companies.pop()
print(companies)
5
companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
companies.discard("DXC")
print(companies)

companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
companies.remove("DXC")
print(companies)

Level2
1
zh = {19, 22, 24, 20, 25, 26}
s = {19, 22, 20, 25, 26, 24, 28, 27}
print(s.union(zh))
#2
zh = {19, 22, 24, 20, 25, 26}
s = {19, 22, 20, 25, 26, 24, 28, 27}
print(zh.intersection(s))
#3
zh = {19, 22, 24, 20, 25, 26}
s = {19, 22, 20, 25, 26, 24, 28, 27}
print(s.issubset(zh))
#4
zh = {19, 22, 24, 20, 25, 26}
s = {19, 22, 20, 25, 26, 24, 28, 27}
print(zh.isdisjoint(s))
#5
zh = {19, 22, 24, 20, 25, 26}
s = {19, 22, 20, 25, 26, 24, 28, 27}
print(zh.union(s))
print(s.union(zh))

Level3
age = [22 , 19 , 24 , 25 , 26 , 24 , 25 , 24]
print(len(age))
print(len(set(age)))
print(len(set(age)) < len(age))
#2
String = '''
Strings are an integrable data structure. 
There are two ways to iterate over the elements of strings by characters and by indexes. 
Each element of the string is represented by one character. 
Strings are an immutable data structure.
'''

List = '''
Lists are ordered. 
The list item can be accessed by index. Lists are mutable types. 
The list can store the number of different elements.
'''

Tuble = '''
Tuples in Python are the same lists with one exception. 
Tuples are immutable data structures. 
Just like lists, they can consist of elements of different types, separated by commas.
Tuples are enclosed in round brackets, not square brackets.
'''

Set = '''
Set is an unordered collection of unique elements. 
Unique, that is, there are no duplicate values in it.
'''
#3
soilem = 'I am a teacher and I love to inspire and teach people'
soilem_set = soilem.split()
soilem = set(soilem_set)
print(soilem)

