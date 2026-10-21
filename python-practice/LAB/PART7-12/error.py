list = []
# list[0] # indexError

text = 'abc'
# number =int(text) # type Error

text = '100%'
try :
    number = int(text)
except ValueError:
    print('{} 는 숫자가 아니네여.'.format(text))

def safe_pop_print(list, index):
    try :
        print(list.pop(index))
    except IndexError:
        print('{} index 못가져와'.format(index))

safe_pop_print([1, 2, 3],5 )
