from abc import ABC, abstractclassmethod
from sqlalchemy.orm import Session

class Repository(ABC):
    
    def __init__(self, session: Session, model):
        self.session = session

    @abstractclassmethod
    def save(self, entity):
        self.session.add(entity)
        self.session.commit()
        self.session.refresh(entity)
        
        return entity
    
    @abstractclassmethod
    def find_by_id(self, id):
        return self.session.query(self.model).get(id)
    
    @abstractclassmethod
    def find_all(self):
        return self.session.query(self.model).all()
    
    @abstractclassmethod
    def update(self, entity):
        self.session.commit()
        self.session.refresh(entity)
        return entity
    
    @abstractclassmethod
    def delete(self, entity):
        self.session.delete(entity)
        self.session.commit()