from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    
    @abstractmethod
    def create_chair(self):
        pass
    
    @abstractmethod
    def create_sofa(self):
        pass
    
    @abstractmethod
    def create_table(self):
        pass


class Chair:

    def __init__(self, name):
        self._name = name
    
    def __str__(self):
        return self._name


class Sofa:

    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name


class Table:

    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name


class VictorianFactory(AbstractFactory):
   
    @abstractmethod
    def create_chair(self):
        return Chair('Victorian chair')

    @abstractmethod
    def create_sofa(self):
        return Sofa('Victorian chair')

    @abstractmethod
    def create_table(self):
        return Table('Victorian chair')


class ModernFactory(AbstractFactory):

    @abstractmethod
    def create_chair(self):
        return Chair('modern chair')

    @abstractmethod
    def create_sofa(self):
        return Sofa('modern chair')

    @abstractmethod
    def create_table(self):
        return Table('modern chair')


class FuturisticFactory(AbstractFactory):

    @abstractmethod
    def create_chair(self):
        return Chair('futuristic chair')

    @abstractmethod
    def create_sofa(self):
        return Sofa('futuristic chair')

    @abstractmethod
    def create_table(self):
        return Table('futuristic chair')


