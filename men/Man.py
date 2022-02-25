from abc import ABC
from person import Person


class Man(Person.Person, ABC):
    Man = list()

    def __init__(self, first_name, last_name, phone, matricule):
        super().__init__(first_name, last_name, phone)
        self.matricule = matricule

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.first_name}', '{self.last_name}', '{self.phone}', '{self.matricule}')"

    def saisir(self):
        first_name = input(" First name : ")
        last_name = input(" Last name : ")
        phone = input(" Phone number : ")
        matricule = input(" Matricule : ")
        return Man(first_name, last_name, phone, matricule)

    def save(self, man, element):
        man.append(element)
        print(f"{element.first_name} was added")

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
                    print(" Element deleted :/")
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
                if item.matricule == matricule:
                    man.remove(item)
                    print(" --- Enter new informations --- ")
                    newinfo = Man.saisir(self)
                    man.append(newinfo)
                    print(" Element edited :/")
                    return
                count = count + 1

            if count == len(man):
                print(" Element not found !!!")

    def display_all(self, man):
        if len(man) <= 0:
            print(" Empty Array !!!")
        else:
            for item in man:
                print(item)
