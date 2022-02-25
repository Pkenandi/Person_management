from person import Person
from abc import ABC


class Woman(Person.Person, ABC):
    Woman = list()

    def __init__(self, first_name, last_name, phone, cin):
        super().__init__(first_name, last_name, phone)
        self.cin = cin

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.first_name}', '{self.last_name}', '{self.phone}', '{self.cin}')"

    def saisir(self):
        first_name = input(" First name : ")
        last_name = input(" Last name : ")
        phone = input(" Phone number : ")
        cin = input(" CIN : ")
        return Woman(first_name, last_name, phone, cin)

    def save(self, woman, element):
        woman.append(element)
        print(f"{element.first_name} was added")

    def display_by(self, woman, cin):
        count = 0
        for item in woman:
            if item.cin == cin:
                print(item)
                return
            count = count + 1

        if count == len(woman):
            print(" Element not found !!!")

    def delete(self, woman, cin):
        if len(woman) <= 0:
            print(" Empty array !!!")
        else:
            count = 0
            for item in woman:
                if item.cin == cin:
                    woman.remove(item)
                    print(" Element deleted :/")
                    return
                count = count + 1

            if count == len(woman):
                print(" Element not found !!!")

    def edit(self, woman, cin):
        if len(woman) <= 0:
            print(f" Empty Array !!!")
        else:
            count = 0
            for item in woman:
                if item.cin == cin:
                    woman.remove(item)
                    print(" --- Enter new informations --- ")
                    newinfo = Woman.saisir(self)
                    woman.append(newinfo)
                    print(" Element edited :/")
                    return
                count = count + 1

            if count == len(woman):
                print(" Element not found !!!")

    def display_all(self, woman):
        if len(woman) <= 0:
            print(" Empty Array !!!")
        else:
            for item in woman:
                print(item)

