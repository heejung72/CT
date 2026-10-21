list2=[37, 23, 10, 33, 29, 40]
print(list2)

list2.append(16)
print(list2)

list3 = list2 + [16]
print(list3)

n = 12
ownership = n in list3
print(ownership)

del list3[12]
list3.remove(40)

del list3[2] # index 값 delete
list3.remove(40) # 40이라는 숫자 remove
