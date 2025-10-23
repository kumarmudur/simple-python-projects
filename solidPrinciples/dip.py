# 5️⃣ Dependency Inversion Principle (DIP)
# Depend on abstractions, not concrete classes.

from abc import ABC, abstractmethod


# ❌ Bad Example

class MySQLDatabase:
    def connect(self):
        print("Connected to MySQL")


class DataProcessor:
    def __init__(self):
        self.db = MySQLDatabase()  # tightly coupled

    def process(self):
        self.db.connect()


# ✅ Good Example

class Database(ABC):
    @abstractmethod
    def connect(self):
        pass


class MySQLDatabase1(Database):
    def connect(self):
        print("Connected to MySQL")


class MongoDB(Database):
    def connect(self):
        print("Connected to MongoDB")


class DataProcessor1:
    def __init__(self, db: Database):
        self.db = db

    def process(self):
        self.db.connect()


# ✅ Now you can inject any database type.

# 💼 Real-World Project Example
# Hospital Management System:
# AppointmentService depends on an abstract Database interface — easily swap MySQL →
# PostgreSQL or even in-memory storage for testing.
