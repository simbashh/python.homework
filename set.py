# st = {'A', 'B', 'C', 'D'}
# st2 = input('in st: ')
# # print(st2 in st)
# if st2 in st:
#     print(f'{st2} we found!')
# else:
#     print(f'{st2} we dont found!')

# st = {'A', 'B', 'C', 'D'}
# st2 = input('What letter do you want to add: ')
# if st2 in st:
#     print(f'{st2} it already exists')
# else:
#     st.add(st2)
#     print(f'{st2} your letter has been added')
#     print(st)

# color = {'green', 'red', 'black'}
# color2 = input("Add your three favorite color:" )
# color.update(color2.split(" "))
# print(color)

color = {'green', 'red', 'black'}
color2 = input("Which letter should remove:" )
if color2 in color:
   print(f'{color2} removed your',color.remove())
else:
   print(f' added random collor:',color.pop())
print(color)


