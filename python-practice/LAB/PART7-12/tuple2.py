a, b = 1, 2

# packing unpacking

c = (3, 4)
print (c)

d, e = c
print(d)
print(e)

x = 5
y = 10

x,y = y,x
print(x)
print(y)

def tuple_funx():
    return 1, 2

q,w = tuple_funx()
print(q, w)
