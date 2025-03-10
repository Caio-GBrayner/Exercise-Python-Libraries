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

    def to_dict(self):
        return {
            "id": self.__id,
            "name": self.__name,
            "email": self.__email,
            "phone": self.__phone
        }

    def __str__(self):
        return f"ID: {self.__id}, Name: {self.__name}, Email: {self.__email}, Phone: {self.__phone}"