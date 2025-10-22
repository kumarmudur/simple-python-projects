# 4️⃣ Interface Segregation Principle (ISP)
# Clients should not be forced to depend on interfaces they do not use.

from abc import ABC, abstractmethod

# ❌ Bad Example


class Worker:
    def work(self):
        pass

    def eat(self):
        pass


class Robot(Worker):
    def work(self):
        print("Robot working")

    def eat(self):
        raise NotImplementedError("Robot doesn’t eat")


# ✅ Good Example
class Workable(ABC):
    @abstractmethod
    def work(self):
        pass


class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass


class Human(Workable, Eatable):
    def work(self):
        print('Human working')

    def eat(self):
        print("Human eating")


class Robot1(Workable):
    def work(self):
        print("Robot working")


# ➡ Each class implements only what it needs.

# 💼 Real-World Project Example
# Factory Automation System:
# Robots only “work,” while Humans “work + eat.”
# Using segregated interfaces keeps your classes clean.


