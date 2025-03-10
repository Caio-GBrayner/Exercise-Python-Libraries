class Member:

    def __init__ (self, id: int, name: str, email: str, phone: str):
        self.__id = id
        self.__name = name
        self.__email = email
        self.__phone = phone

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
    def email(self):
        return self.__email

    @email.setter
    def email(self, email: str):
        __email = email

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone: str):
        __phone = phone