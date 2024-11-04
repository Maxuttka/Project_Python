import abc

class MoveObject(abc.ABC):
    @abc.abstractmethod
    def move(self):
        pass

class DrawObject(abc.ABC):
    @abc.abstractmethod
    def draw(self):
        pass

class InitObject(abc.ABC):
    @abc.abstractmethod
    def __init__(self):
        pass