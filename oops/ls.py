import json
from datetime import datetime, timedelta
import tkinter as tk
from tkinter import messagebox, ttk


# ---------- Book Class ----------
class Book:
    def __init__(self, book_id, title, author, available=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = available

    def to_dict(self):
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "available": self.available
        }

    @staticmethod
    def from_dict(data):
        return Book(data["book_id"], data["title"], data["author"], data["available"])


# ---------- Borrower Class ----------
class Borrower:
    def __init__(self, user_id, name, borrowed_books=None):
        self.user_id = user_id
        self.name = name
        self.borrowed_books = borrowed_books or {}

    def borrow_book(self, book, due_date):
        if book.book_id in self.borrowed_books:
            return False, f"{self.name} already borrowed '{book.title}'."
        self.borrowed_books[book.book_id] = due_date.strftime("%Y-%m-%d")
        return True, f"{self.name} borrowed '{book.title}' (Due: {due_date.date()})"

    def return_book(self, book_id):
        return self.borrowed_books.pop(book_id, None)

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "name": self.name,
            "borrowed_books": self.borrowed_books
        }

    @staticmethod
    def from_dict(data):
        return Borrower(data["user_id"], data["name"], data["borrowed_books"])


# ---------- Library Class ----------
class Library:
    PENALTY_PER_DAY = 10
    DATA_FILE = "library_data.json"

    def __init__(self):
        self.books = {}
        self.borrowers = {}
        self.load_data()

    def save_data(self):
        data = {
            "books": [book.to_dict() for book in self.books.values()],
            "borrowers": [borrower.to_dict() for borrower in self.borrowers.values()]
        }
        with open(self.DATA_FILE, "w") as f:
            json.dump(data, f, indent=4)

    def load_data(self):
        try:
            with open(self.DATA_FILE, "r") as f:
                data = json.load(f)
            self.books = {b["book_id"]: Book.from_dict(b) for b in data["books"]}
            self.borrowers = {u["user_id"]: Borrower.from_dict(u) for u in data["borrowers"]}
        except FileNotFoundError:
            pass

    def add_book(self, title, author):
        book_id = len(self.books) + 1
        self.books[book_id] = Book(book_id, title, author)
        self.save_data()
        return f"Book '{title}' added successfully!"

    def add_borrower(self, name):
        user_id = len(self.borrowers) + 1
        self.borrowers[user_id] = Borrower(user_id, name)
        self.save_data()
        return f"Borrower '{name}' added successfully!"

    def borrow_book(self, user_id, book_id):
        if user_id not in self.borrowers:
            return False, "Borrower not found!"
        if book_id not in self.books:
            return False, "Book not found!"

        borrower = self.borrowers[user_id]
        book = self.books[book_id]

        if not book.available:
            return False, f"'{book.title}' is already borrowed!"

        due_date = datetime.now() + timedelta(days=14)
        book.available = False
        success, msg = borrower.borrow_book(book, due_date)
        self.save_data()
        return success, msg

    def return_book(self, user_id, book_id):
        if user_id not in self.borrowers or book_id not in self.books:
            return False, "Invalid borrower or book ID!"

        borrower = self.borrowers[user_id]
        book = self.books[book_id]
        due_date_str = borrower.return_book(book_id)

        if not due_date_str:
            return False, f"{borrower.name} did not borrow '{book.title}'."

        book.available = True
        due_date = datetime.strptime(due_date_str, "%Y-%m-%d")
        penalty = self.calculate_penalty(due_date)
        self.save_data()

        if penalty > 0:
            return True, f"Book returned late! Penalty: ₹{penalty}"
        return True, "Book returned successfully!"

    def calculate_penalty(self, due_date):
        today = datetime.now()
        if today > due_date:
            days_late = (today - due_date).days
            return days_late * self.PENALTY_PER_DAY
        return 0

    def get_available_books(self):
        return [b for b in self.books.values() if b.available]


# ---------- GUI Class ----------
class LibraryApp:
    def __init__(self, root):
        self.library = Library()
        self.root = root
        self.root.title("📚 Library Management System")
        self.root.geometry("800x600")
        self.root.config(bg="#f5f5f5")

        self.setup_ui()
        self.refresh_books()

    def setup_ui(self):
        tk.Label(self.root, text="Library Management System", font=("Arial", 20, "bold"), bg="#f5f5f5").pack(pady=10)

        frame = tk.Frame(self.root, bg="#f5f5f5")
        frame.pack(pady=10)

        # --- Add Book ---
        tk.Label(frame, text="Book Title:").grid(row=0, column=0)
        self.book_title = tk.Entry(frame, width=25)
        self.book_title.grid(row=0, column=1, padx=5)

        tk.Label(frame, text="Author:").grid(row=0, column=2)
        self.book_author = tk.Entry(frame, width=25)
        self.book_author.grid(row=0, column=3, padx=5)

        tk.Button(frame, text="Add Book", command=self.add_book, bg="#4CAF50", fg="white").grid(row=0, column=4, padx=10)

        # --- Add Borrower ---
        tk.Label(frame, text="Borrower Name:").grid(row=1, column=0, pady=10)
        self.borrower_name = tk.Entry(frame, width=25)
        self.borrower_name.grid(row=1, column=1)
        tk.Button(frame, text="Add Borrower", command=self.add_borrower, bg="#2196F3", fg="white").grid(row=1, column=4)

        # --- Borrow / Return ---
        tk.Label(frame, text="User ID:").grid(row=2, column=0, pady=10)
        self.user_id_entry = tk.Entry(frame, width=10)
        self.user_id_entry.grid(row=2, column=1)

        tk.Label(frame, text="Book ID:").grid(row=2, column=2)
        self.book_id_entry = tk.Entry(frame, width=10)
        self.book_id_entry.grid(row=2, column=3)

        tk.Button(frame, text="Borrow Book", command=self.borrow_book, bg="#FFC107").grid(row=2, column=4)
        tk.Button(frame, text="Return Book", command=self.return_book, bg="#FF5722", fg="white").grid(row=2, column=5, padx=5)

        # --- Books Table ---
        self.tree = ttk.Treeview(self.root, columns=("ID", "Title", "Author"), show="headings", height=15)
        self.tree.heading("ID", text="Book ID")
        self.tree.heading("Title", text="Title")
        self.tree.heading("Author", text="Author")
        self.tree.pack(pady=20, fill=tk.BOTH, expand=True)

    def refresh_books(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        for book in self.library.get_available_books():
            self.tree.insert("", tk.END, values=(book.book_id, book.title, book.author))

    def add_book(self):
        title = self.book_title.get().strip()
        author = self.book_author.get().strip()
        if not title or not author:
            messagebox.showwarning("Warning", "Please fill both title and author.")
            return
        msg = self.library.add_book(title, author)
        messagebox.showinfo("Success", msg)
        self.refresh_books()
        self.book_title.delete(0, tk.END)
        self.book_author.delete(0, tk.END)

    def add_borrower(self):
        name = self.borrower_name.get().strip()
        if not name:
            messagebox.showwarning("Warning", "Please enter borrower name.")
            return
        msg = self.library.add_borrower(name)
        messagebox.showinfo("Success", msg)
        self.borrower_name.delete(0, tk.END)

    def borrow_book(self):
        try:
            user_id = int(self.user_id_entry.get())
            book_id = int(self.book_id_entry.get())
            success, msg = self.library.borrow_book(user_id, book_id)
            messagebox.showinfo("Result", msg)
            self.refresh_books()
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric IDs.")

    def return_book(self):
        try:
            user_id = int(self.user_id_entry.get())
            book_id = int(self.book_id_entry.get())
            success, msg = self.library.return_book(user_id, book_id)
            messagebox.showinfo("Result", msg)
            self.refresh_books()
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric IDs.")


# ---------- Run App ----------
if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()