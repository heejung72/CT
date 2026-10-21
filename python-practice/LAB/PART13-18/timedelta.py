import datetime

# 오늘부터 100일 후는 언제니?

hundred = datetime.timedelta(days=100)
print(datetime.datetime.now() + hundred)

print(type(datetime.datetime.now()))

# timedelta + datetime 가능

hundred_before = datetime.timedelta(days=-100)
print(datetime.datetime.now()+hundred_before)

tomorrow = datetime.datetime.now().replace(hour = 9, minute = 0, second = 1) + datetime.timedelta(days=1)
print(tomorrow)
