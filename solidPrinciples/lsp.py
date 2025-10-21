# 3️⃣ Liskov Substitution Principle (LSP)
# Subclasses should be replaceable for their parent classes without breaking the program.
# ❌ Bad Example
class Bird:
    def fly(self):
        print("Flying")


# 🧨 Violates LSP — a Penguin can’t behave like a Bird that can fly.
class Penguin(Bird):
    def fly(self):
        raise Exception("Penguins can’t fly!")


# ✅ Good Example
class Bird:
    pass


class FlyingBird(Bird):
    def fly(self):
        print("Flying")


class Penguin1(Bird):
    def swim(self):
        print("Swimming")


# ➡ Now, substituting subclasses doesn’t break behavior.


