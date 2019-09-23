newChance = True

while newChance == True:
    try:
        age = int(input('Enter your age: '))
        break;
    except ValueError:
        print ('You have to enter a number!')
        try:
            startOver = int(input('To start over, enter 0. To exit, press any other key. '))
        except:
            print('OK, you do not want to start over, see you soon!')
            newChance = False
        else:
            if startOver == 0:
                newChance = True
            else:
                print('OK, you do not want to start over, see you soon!')
                newChance = False

print("You will be " + str(age+10) + " in ten years")