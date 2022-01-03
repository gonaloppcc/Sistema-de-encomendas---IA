menu_options = {
    1: 'Option 1',
    2: 'Option 2',
    3: 'Option 3',
    4: 'Exit',
}


def print_menu():
    for key in menu_options.keys():
        print(key, '--', menu_options[key])


def option1():
    print('Opção \'Menu 1\'')


def option2():
    print('Opção \'Menu 2\'')


def option3():
    print('Opção \'Menu 3\'')


if __name__ == '__main__':
    while (True):
        print_menu()
        option = ''
        try:
            option = int(input('Escolha uma opção: '))
        except:
            print('Input incorreto. Por favor introduza um número...')
        # Check what choice was entered and act accordingly
        if option == 1:
            option1()
        elif option == 2:
            option2()
        elif option == 3:
            option3()
        elif option == 4:
            print('Adeus...')
            exit()
        else:
            print('Opção invélida, tente novamete.')
