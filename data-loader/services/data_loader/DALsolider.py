import uuid

class Solider:

    def __init__(self ,first_name:str ,last_name:str ,phone_number:str ,rank:str):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.rank = rank
        self.ID = uuid.uuid4()


    





