from exceptions.member_exceptions import MemberNotFoundError, DuplicateEmailError 
from entities.member import Member

class MemberService:
    def __init__(self, member_repository):

        self.member_repository = member_repository

    def create_member(self, name, email, phone):
       
        existing_member = self.member_repository.find_by_email(email)
        if existing_member:
            raise DuplicateEmailError(f"E-mail '{email}' is already in use.")

        new_member = Member(name=name, email=email, phone=phone)
        return self.member_repository.save(new_member)

    def get_member_by_id(self, id):

        member = self.member_repository.find_by_id(id)
        if not member:
            raise MemberNotFoundError(f"Member id {id} not found.")
        return member

    def get_all_members(self):

        return self.member_repository.find_all()

    def update_member(self, id, name=None, email=None, phone=None):
       
        member = self.member_repository.find_by_id(id)
        if not member:
            raise MemberNotFoundError(f"Member id {id} not found.")

        if name:
            member.name = name
        if email:
            member.email = email
        if phone:
            member.phone = phone

        return self.member_repository.update(member)

    def delete_member(self, id):
    
        member = self.member_repository.find_by_id(id)
        if not member:
            raise MemberNotFoundError(f"Member id {id} not found.")

        self.member_repository.delete(member)