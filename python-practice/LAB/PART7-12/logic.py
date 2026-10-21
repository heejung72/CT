def return_false():
    print("함수 return_false")
    return False

def return_true():
    return True

if return_true() and return_false():
    print(True)
else :
    print(False)

print(bool(0))
print(bool(1))

