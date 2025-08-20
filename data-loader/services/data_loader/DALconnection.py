from pymongo import MongoClient
from services.data_loader import config

class Connections:
    
    def __init__(self):

        self.client = None
        self.db = None

    def connection_db(self):
        try:
            self.client = MongoClient(config.MONGODB_HOST ,config.MONGODB_PORT)
            self.db = self.client(config.MONGODB_DATABASE)
            return self.db
        except Exception as e:
            raise ConnectionError(f"ERROR: From Connections.connection_db :{e}")

    def get_server_health(self):
        try:
            if not self.client:
                return False
            self.client.admin.command("ping")
            return True
        except Exception as e:
            print(f"error in server health: {e}")
            return False

    def disconnect(self):
        """
        Close database connection
        """
        if self.client:
            self.client.close()