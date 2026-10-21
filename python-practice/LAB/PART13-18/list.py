list1 = [135, 462, 27, 2753, 234]

list1.index(27)

# list1.index(50)

if 50 in list1:
    list1.index(50)

list2=[1,2,3] + [4,5,6]
print(list2)

list1.extend([9,10,11])
print(list1)

list1.insert(2, 999)
# index에 값 넣음

list1.insert(99999, 55)
# index를 한참 넘어가는 크기에 넣으면 맨 마지막에 감

list.reverse()
