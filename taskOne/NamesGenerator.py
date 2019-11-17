class NamesGenerator:

    def __init__(self):
        self.firstNames = set()
        self.lastNames = set()

    def ask_input(self):
        firstname = input('Please enter a first name: ')
        lastname = input('Please enter a last name: ')
        return firstname, lastname


    def add_new_first_name(self, firstname):
        self.firstNames.add(firstname)

    def add_new_last_name(self, lastname):
        self.lastNames.add(lastname)

    def get_list_of_full_names(self):

        fullnames = []

        for firstname in self.firstNames:
            for lastname in self.lastNames:
                # print(firstname+lastname)
                fullnames.append(firstname + " " + lastname)

        return fullnames
