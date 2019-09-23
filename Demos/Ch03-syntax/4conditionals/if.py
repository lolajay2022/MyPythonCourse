a = 3
b = 5

if a < b:
    print('a is less than b')
elif a > b:
    print('a is greater than b')
else:
    print('a is equal to b')
            

today = 'Monday'
is_holiday = False;

if today == 'Monday' and is_holiday == False:
    print('Go to work!')


if today != 'Sunday' and today != 'Saturday' and is_holiday == False:
    print('Go to work!')


if today == 'Sunday' or today == 'Saturday':
    print('Enjoy the weekend!')   


if not (today == 'Sunday' or today == 'Saturday'):
    print('Go to work!')        

if today != 'Sunday' and today != 'Saturday':
    print('Go to work!')

    