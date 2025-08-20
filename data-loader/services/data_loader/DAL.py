import pymongo
import config
from services.data_loader.DALconnection import Connections
from services.data_loader.DALsolider import Solider

class DAL:

    def __init__(self):
        self.db_connection = Connections()
        self.database = self.db_connection.connection_db()
        self.collection = self.database[config.MONGODB_COLLECTION]

    def create_collection(self ,solider:Solider):
        try:
            document = self.collection.insert_one(solider.to_dict())
            return document.acknowledged
        except Exception as e:
            print(f"ERROR: From DAL.create_collection: {e}")
            return False

    def read_document_by_ID(self ,solider_id ):
        try:
            result = self.collection.find_one({"id": solider_id})
            if result:
                return Solider.from_dict(result)
            return None
        except Exception as e:
            print(f"ERROR: From DAL.read_document_by_ID: {e}")
            return None

    def update_document_by_ID(self ,doc_id: str, update_data: dict) -> bool:
        try:
            result = self.collection.update_one(
                {"_id": doc_id},
                {"$set": update_data}
            )
            return result.modified_count > 0
        except Exception as e:
            print(f"ERROR: From DAL.update_document_by_ID: {e}")
            return False

    def delete_document_by_ID(self, solider_id: str) -> bool:
        try:
            result = self.collection.delete_one({"id": solider_id})
            return result.deleted_count > 0
        except Exception as e:
            print(f"ERROR: From DAL.delete_document_by_ID: {e}")
            return False
        
    def show_all_collection(self):
        try:
            results = self.collection.find({},{"_id":0})
            return [result for result in results if result]
        
        except Exception as e:
            print(f"ERROR: From DAL.read_collection: {e}")
            return None

    def close_connection(self):
        """
        Close database connection
        """
        self.db_connection.disconnect()
