from .topic import Topic
from .category import Category
from .document import Document
from typing import List, Dict


def common_add(instance, object_):
    if isinstance(object_, Category):
        if object_.id in instance.category_by_id:
            return

        instance.categories.append(object_)
        instance.category_by_id[object_.id] = object_

    elif isinstance(object_, Topic):
        if object_.id in instance.topic_by_id:
            return

        instance.topics.append(object_)
        instance.topic_by_id[object_.id] = object_

    elif isinstance(object_, Document):
        if object_.id in instance.document_by_id:
            return

        instance.documents.append(object_)
        instance.document_by_id[object_.id] = object_


def common_edit(instance, object_type, *args):
    if object_type == Category:
        category_id, new_name = args
        instance.category_by_id[category_id].edit(new_name)

    elif object_type == Topic:
        topic_id, new_topic, new_storage_folder = args
        instance.topic_by_id[topic_id].edit(new_topic, new_storage_folder)

    elif object_type == Document:
        document_id, new_file_name = args
        instance.document_by_id[document_id].edit(new_file_name)


def common_delete(instance, object_type, id):
    if object_type == Category:
        category = instance.category_by_id[id]

        instance.categories.remove(category)
        del instance.category_by_id[id]

    if object_type == Topic:
        topic = instance.topic_by_id[id]

        instance.topics.remove(topic)
        del instance.topic_by_id[id]

    if object_type == Document:
        document = instance.document_by_id[id]

        instance.documents.remove(document)
        del instance.document_by_id[id]


class Storage:
    categories: List[Category]
    topics: List[Topic]
    documents: List[Document]

    category_by_id: Dict[int, Category]
    topic_by_id: Dict[int, Topic]
    document_by_id: Dict[int, Document]

    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

        self.category_by_id = {}
        self.topic_by_id = {}
        self.document_by_id = {}

    def add_category(self, category: Category):
        common_add(self, category)

    def add_topic(self, topic: Topic):
        common_add(self, topic)

    def add_document(self, document: Document):
        common_add(self, document)

    def edit_category(self, category_id: int, new_name: str):
        common_edit(self, Category, category_id, new_name)

    def edit_topic(self, topic_id: int, new_topic: int, new_storage_folder: str):
        common_edit(self, Topic, topic_id, new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str):
        common_edit(self, Document, document_id, new_file_name)

    def delete_category(self, category_id: int):
        common_delete(self, Category, category_id)

    def delete_topic(self, topic_id: int):
        common_delete(self, Topic, topic_id)

    def delete_document(self, document_id: int):
        common_delete(self, Document, document_id)

    def get_document(self, document_id):
        return self.document_by_id[document_id]

    def __repr__(self):
        return '\n'.join([str(doc) for doc in self.documents])
