class Library:

    # Initialize a constructor
    def __init__(self, list, name):
        self.booksList = list
        self.name = name
        self.bookslend = {}

    # To display the books available in a library
    def displayBooks(self):
        print(f"We have the following books in our collection at {self.name}:")
        for book in self.booksList:
            print(book)

    # To add book in a library
    def addBook(self, book):
        self.booksList.append(book)
        print(f"{book} has been added to the collection!")

    # To lend a Book
    def lendBook(self, book, user):
        if book not in self.bookslend.keys():
            self.bookslend.update({book:user})
            print("The database has been updated. You can take the book now!")
        else:
            print(f"Apologies! The book is not available, it's already lent by {self.bookslend[book]}")

    # To return a Book
    def returnBook(self, book):
        self.bookslend.pop(book)
        print("The book has been returned successfully!")


if __name__ == '__main__':
    arshad = Library(["Hands on Machine Learning", "Rich Dad Poor Dad", "C++ basics", "Harry Potter", "Macbeth"], "The Arshad Library")

    # An infinite loop to use the Library repeatedly
    while True:
        valid_entries = ['1', '2', '3', '4']
        print(f"Welcome to {arshad.name}!\n"
              "1. Display the books\n"
              "2. Add a book\n"
              "3. Lend a Book\n"
              "4. Return a book\n"
              "Q to Quit")
        userInput = input("Enter the option you want to proceed with:\n").lower()

        if userInput == 'q':
            exit()

        elif userInput not in valid_entries:
            print("Enter a valid input!")

        elif userInput == '1':
            arshad.displayBooks()

        elif userInput == '2':
            book = input("Enter the name of the book:\n")
            arshad.addBook(book)

        elif userInput == '3':
            book = input("Enter the name of the book you want to borrow:\n")
            user = input("Enter your name:\n")
            arshad.lendBook(book, user)

        elif userInput == '4':
            book = input("Enter the name of the book you want to return:\n")
            arshad.returnBook(book)