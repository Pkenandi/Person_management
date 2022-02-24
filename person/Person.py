from abc import ABC, abstractmethod


class Person(ABC):
    Persons = []

    def __init__(self):
        self.first_name = None
        self.last_name = None
        self.phone = None

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.first_name} {self.last_name} {self.phone}')"

    @abstractmethod
    def saisir(self):
        self.first_name = input(" First name : ")
        self.last_name = input(" Last name : ")
        self.phone = input(" Phone number : ")
        return self

    @abstractmethod
    def save(self, array, element):
        pass

    @abstractmethod
    def display_all(self, element):
        pass

    @abstractmethod
    def display_by(self, array, attribute):
        pass

    @abstractmethod
    def delete(self, array, element):
        pass
        # if len(Person.Persons) <= 0:
        #     print(f" Empty Array !!!")
        # else:
        #     for person in Person.Persons:
        #         if person.phone == phone:
        #             Person.Persons.remove(person)
        #             print(f" {person.first_name} was deleted from database :/")

    @abstractmethod
    def edit(self, array, element):
        pass

