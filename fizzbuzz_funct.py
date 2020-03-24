
def bizzzzuu(num):
    while True:
        try:
            if 'penpinapplespen' == num:
                print('Thank you for playing. Bye!')
                break
            elif num <=0:
                raise ValueError
            else:
                for i in range(int(num)):
                    composite = ''
                    if ((i + 1) % 3) == 0:
                        composite = 'bizz'
                    if ((i + 1) % 5) == 0:touch
                        composite += 'zzuu'
                    print(i + 1, composite)
            break
        except TypeError:
            num = input('Please enter a number!\nEnter \'penpinapplespen\' to exit.\n')
        except ValueError:
            num = input('Please enter a number!\nEnter \'penpinapplespen\' to exit.\n')