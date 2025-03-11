from sqlalchemy.orm import Session

class Repository:
    
    def __init__(self, session: Session, model):
        self.session = session

    def save(self, entity):
        self.session.add(entity)
        self.session.commit()
        self.session.refresh(entity)
        
        return entity
    
    def find_by_id(self, id):
        return self.session.query(self.model).get(id)
    
    def find_all(self):
        return self.session.query(self.model).all()
    
    def update(self, entity):
        self.session.commit()
        self.session.refresh(entity)
        return entity
    
    def delete(self, entity):
        self.session.delete(entity)
        self.session.commit()