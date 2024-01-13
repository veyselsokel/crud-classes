import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

class FirebaseCRUD:
    def __init__(self, collection_name):
        self.collection_name = collection_name
        self.db = self._get_firestore_db()

    def _get_firestore_db(self):
        cred = credentials.Certificate("crud-class-firebase-adminsdk-sednr-24f32980ae.json")
        firebase_admin.initialize_app(cred)
        return firestore.client()

    def create(self, data):
        doc_ref = self.db.collection(self.collection_name).document()
        doc_ref.set(data)
        return doc_ref.id

    def read(self, doc_id):
        doc_ref = self.db.collection(self.collection_name).document(doc_id)
        doc = doc_ref.get()
        if doc.exists:
            return doc.to_dict()
        else:
            return None

    def update(self, doc_id, data):
        doc_ref = self.db.collection(self.collection_name).document(doc_id)
        doc_ref.update(data)

    def delete(self, doc_id):
        doc_ref = self.db.collection(self.collection_name).document(doc_id)
        doc_ref.delete()