from project.category import Category
from project.document import Document
from project.storage import Storage
from project.topic import Topic

c1 = Category(1, "work")
t1 = Topic(1, "daily tasks", "C:\\work_documents")
d1 = Document(1, 1, 1, "finilize project")
d1.add_tag("Kose")
d1.add_tag("Bose")
d1.add_tag("Bose")


storage = Storage()

storage.add_category(c1)
storage.add_topic(t1)
storage.add_document(d1)

storage.edit_category(c1.id, "Hello")
storage.edit_topic(t1.id, "Hello", "World")

storage.edit_document(1, "Ivailo Buzata")
storage.delete_category(t1.id)
print(d1)
print(c1)
print(t1)
storage.delete_document(1)
print(storage)
