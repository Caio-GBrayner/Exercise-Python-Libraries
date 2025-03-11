
from sqlalchemy.orm import Session
from entities.member import Member
from .repository import Repository


class MemberRepository(Repository):
    def __init__(self, session: Session):
        super().__init__(session, Member)

    def find_by_email(self, email: str):
         return self.session.query(Member).filter(Member.email == email).first()