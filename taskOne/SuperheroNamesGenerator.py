from taskOne.NamesGenerator import NamesGenerator
from exceptions.CustomExceptions import NameSoUglyApplicationCrashedError


class SuperheroNamesGenerator(NamesGenerator):

    def ask_input(self):
        fn, ln = input('Please enter a first name: '), input('Please enter a last name: ')
        fullname = fn + ln
        if fullname[-3:] != 'man':
            raise NameSoUglyApplicationCrashedError(fullname)

        return fn, ln
