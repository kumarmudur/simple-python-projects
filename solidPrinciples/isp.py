# 4️⃣ Interface Segregation Principle (ISP)
# Clients should not be forced to depend on interfaces they do not use.

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
