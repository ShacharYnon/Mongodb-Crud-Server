import uuid

class Solider:

    def __init__(self ,first_name:str ,last_name:str ,phone_number:str ,rank:str):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.rank = rank
        self.ID = str(uuid.uuid4())

    def to_dict(self):
        return{
            "first_name" : self.first_name,
            "last_name" : self.last_name,
            "phone_number" : self.phone_number,
            "rank" : self.rank,
            "id": self.ID
        }
        




