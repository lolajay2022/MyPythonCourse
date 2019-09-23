num_list = [111, 222, 333]
alpha_list = ['a', 'b', 'c']


def nested_loop():
    for number in num_list:
        print(number)
        for letter in alpha_list:
            print(letter)

if __name__ == '__main__':
    nested_loop()