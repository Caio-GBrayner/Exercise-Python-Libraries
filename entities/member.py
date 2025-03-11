from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base

class Member(Base):

    __tablename__ = 'member'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone = Column(String(20), nullable=False)

    def __init__ (self, name: str, email: str, phone: str, id: int = None):
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
    
    def __eq__(self, other):
        if not isinstance(other, Member):
            return False
        return self.id == other.id and self.name == other.name and self.email == other.email and self.phone == other.phone

    def __hash__(self):
        return hash((self.id, self.name, self.email, self.phone))

    def __str__(self):
        return f"ID: {self.__id}, Name: {self.__name}, Email: {self.__email}, Phone: {self.__phone}"