from zoneinfo import available_timezones


class Book:
    def __init__(self, id: int, title: str, publisher: str, gender: str):
        self.__id = id
        self.__title = title
        self.__publisher = publisher
        self.__gender = gender
        self.__available = True

    @property
    def available(self):
        return self.__available

    @available.setter
    def available(self, value):
        self.__available = value

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__title

    @name.setter
    def name(self, title: str):
        __title = title

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
            "name": self.__title,
            "publisher": self.__publisher,
            "gender": self.__gender
        }

def __str__(self):
    return f"ID: {self.__id}, Name: {self.__name}, Publisher: {self.__publisher}, Gender: {self.__gender}"