from abc import ABC
import array as arr

from person import Person


class Man(Person.Person, ABC):
    Man = []

    def __init__(self):
        super().__init__()
        self.matricule = None

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.first_name}', '{self.last_name}', '{self.phone}', '{self.matricule}')"

    def saisir(self):
        super().saisir()
        self.matricule = input(" Matricule : ")
        return self

    def save(self, man, element):
        # if len(man) <= 0:
        count = 0
        while count <= len(man):
            count = count + 1

        man.insert(count, element)
        print(f"{element.first_name} was added")

    # else:
    #     count = 0
    #     for item in man:
    #         if item.first_name == element.first_name \
    #                 or item.last_name == element.last_name \
    #                 or item.phone == element.phone \
    #                 or item.matricule == element.matricule:
    #             print(" Element already exist")
    #             return
    #         count = count + 1
    #
    #     if len(man) == count:
    #         man.append(element)
    #         print(f"{element.first_name} was added")
    # print(man)

    def display_by(self, man, matricule):
        count = 0
        for item in man:
            if item.matricule == matricule:
                print(item)
                return
            count = count + 1

        if count == len(man):
            print(" Element not found !!!")

    def delete(self, man, matricule):
        if len(man) <= 0:
            print(" Empty array !!!")
        else:
            count = 0
            for item in man:
                if item.matricule == matricule:
                    man.remove(item)
                    return
                count = count + 1

            if count == len(man):
                print(" Element not found !!!")

    def edit(self, man, matricule):
        if len(man) <= 0:
            print(f" Empty Array !!!")
        else:
            count = 0
            for item in man:
                if item.first_name == matricule:
                    man.remove(item)
                    print(" --- Enter new informations --- ")
                    Man.saisir(self)
                    man.append(self)
                    print(" Element edited :/")
                    return
                count = count + 1

            if count == len(man):
                print(" Element not found !!!")

    def display_all(self, man):
        for item in man:
            print(item)
