class Books:
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
