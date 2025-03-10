class Book:
    def __init__(self, id: int, name: str, publisher: str, gender: str):
        self.__id = id
        self.__name = name
        self.__publisher = publisher
        self.__gender = gender


    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        __name = name

    @property
    def publisher(self):
        return self.__publisher

    @publisher.setter
    def publisher(self, publisher: str):
        __publisher = publisher

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, gender: str):
        __gender = gender

    def to_dict(self):
        return {
            "id": self.__id,
            "name": self.__name,
            "publisher": self.__publisher,
            "gender": self.__gender
        }

def __str__(self):
    return f"ID: {self.__id}, Name: {self.__name}, Publisher: {self.__publisher}, Gender: {self.__gender}"