from taskOne.NamesGenerator import NamesGenerator
from taskOne.SuperheroNamesGenerator import SuperheroNamesGenerator

# global variable
runapp = True
ng = NamesGenerator()
sng = SuperheroNamesGenerator()

# unassigned variables gets ignored so using this as comment
"""
function just used for asking firstnames
and lastnames and returning them 
"""

# main function which asks for names
# in loop, validates them and saves them in set
def name_adding_unit(isSuperheroName):
    global runapp  # telling this function to use global variable
    global ng

    while runapp:

        # variables are declared only inside 'if' statements
        # why is this working outside 'if'??
        if not isSuperheroName:
            fn, ln = ng.ask_input()
        else:
            fn, ln = sng.ask_input()

        if not fn.isalpha() or not ln.isalpha():
            print("ERROR! Alphabetical values only.")
        else:
            ng.add_new_first_name(fn)
            ng.add_new_last_name(ln)

        goon = input('Would you like to add another name?(y/n) ')

        runapp = goon == 'y'

    runapp = True


# method just responsible to print menu and  return selected menu item
def menu_unit():
    print()
    print('###################################')
    print('------------- MENU ----------------')
    print('enter 1 -> Add new names')
    print('enter 2 -> Add a new Superhero names')
    print('enter 3 -> List all names combo')
    print('enter 4 -> Get longest name in the list')
    print('enter 5 or more -> Exit')
    print('###################################')
    print()

    res = input('Enter your choice: ')
    if not res.isnumeric():
        print("Error! Please Enter Numbers only")
        menu_unit()
    else:
        return int(res)

def main():
    global ng
    mainloop = True

    while mainloop:
        response = menu_unit()
        if response == 1:
            name_adding_unit(False)
        elif response == 2:
            name_adding_unit(True)
        elif response == 3:
            print()
            print("All combined names:")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            for fullname in ng.get_list_of_full_names():
                print(fullname)
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        elif response == 4:
            try:
                longest_name = max(ng.get_list_of_full_names(), key=len)
                print('\n', f'Longest name in the list belongs to "{longest_name}"')
            except Exception as e:
                print("ERROR! List is empty. Please add some names first!")

        else:
            mainloop = False


if __name__ == '__main__':
    main()
