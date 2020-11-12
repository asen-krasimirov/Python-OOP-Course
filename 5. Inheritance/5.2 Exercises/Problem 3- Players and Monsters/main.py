from project import *

objects = [
    Hero('username1', 1),
    Elf('username2', 2),
    MuseElf('username3', 3),
    Wizard('username4', 4),
    DarkWizard('username5', 5),
    SoulMaster('username6', 6),
    Knight('username7', 7),
    DarkKnight('username8', 8),
    BladeKnight('username9', 9),
]


def attribute_presence_test():
    for object_ in objects:
        assert hasattr(object_, 'username'), "had to username"
        assert hasattr(object_, 'level'), "had to level"
    print('passed')


def _repr_method_test():
    for object_ in objects:
        class_name = object_.__class__.__name__
        content = object_.__dict__
        print(f"Class Name: {class_name}")
        # print(f"Content: {content}")
        print(object_)
    print('passed')


print("first test")
attribute_presence_test()
print("second test")
_repr_method_test()

