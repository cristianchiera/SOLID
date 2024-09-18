from abc import ABC, abstractmethod

class Worker(ABC):
    @abstractmethod
    def work(self):
        pass

class Eater(ABC):
    @abstractmethod
    def eat(self):
        pass

class Robot(Worker):
    def work(self):
        return "Robot trabajando"

class Human(Worker, Eater):
    def work(self):
        return "Humano trabajando"

    def eat(self):
        return "Humano comiendo"

# Uso de las clases
robot = Robot()
human = Human()

print(robot.work())
print(human.work())
print(human.eat())
