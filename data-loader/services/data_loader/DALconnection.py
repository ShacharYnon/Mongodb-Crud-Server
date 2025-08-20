from pymongo import MongoClient


class Connections:
    
    def __init__(self,connection:str,database_name:str):
        self.client = MongoClient(connection)
        self.db = self.client[database_name]
    
    def get_server_health(self):
        try:
            if not self.client:
                return False
            self.client.admin.command("ping")
            return True
        except Exception as e:
            print(f"error in server health: {e}")
            return False

    def show_collection(self,collection_name:str):
        try:
            collection =list(self.db[collection_name].find({}))
            return collection
        except Exception as e:
            print(f"error in show collections {e}")