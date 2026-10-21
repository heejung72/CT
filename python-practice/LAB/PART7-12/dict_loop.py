seasons = ['봄', '여름', '가을' ,'겨울']

for season in seasons:
    print(season)

ages= {'Tod':30 ,'Hee':20, 'Paul':22}

for key in ages.keys():
    print(key)

for value in ages.values():
    print(value)

for key in ages.keys():
    print('{}, {}'.format(key, ages[key]))

for key,value in ages.items():
    print('{} {}'.format(key,value))
