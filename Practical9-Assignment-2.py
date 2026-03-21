class Book:
    def __init__(self, title):
        self.title = title
        self.available = True


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title):
        self.books.append(Book(title))
        print("Book added!")

    def show_books(self):
        for b in self.books:
            print(b.title, "-", "Available" if b.available else "Not Available")

    def lend_book(self, title):
        for b in self.books:
            if b.title == title and b.available:
                b.available = False
                print("Book issued")
                return
        print("Book not available")

    def return_book(self, title):
        for b in self.books:
            if b.title == title:
                b.available = True
                print("Book returned")
                return


lib = Library()

while True:
    print("\n1.Add Book 2.Show Books 3.Lend 4.Return 5.Exit")
    ch = input("Enter choice: ")

    if ch == '1':
        lib.add_book(input("Enter book name: "))
    elif ch == '2':
        lib.show_books()
    elif ch == '3':
        lib.lend_book(input("Enter book name: "))
    elif ch == '4':
        lib.return_book(input("Enter book name: "))
    elif ch == '5':
        break
