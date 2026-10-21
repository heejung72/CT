my_list = [1, 2, 3, 4, 5, 6]
print(my_list[0])

print(my_list[1])

str = "Hello World"
print(str)
print(str[0])
print(str[1])
print ("3" in str)
print (4 in my_list)

print("H" in str)
print("Z" in str)

print(my_list.index(5))
print(str.index("r"))

characters = list("abcdef")
print(characters)
words ="Hello World 는 프로그래밍을 배우기에 아주 좋은 사이트입니다."
word_list = words.split()
print(word_list)

word = words.split(" ")
print(word)

print(":".join(word))
