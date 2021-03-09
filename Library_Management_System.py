class Library:
    def __init__(self, listOfBooks):

        self.books = listOfBooks

    def displayBooks(self):
        print("Books present in this library at this time are: ")
        for books in self.books:
            print("*  " + books)

    def borrowBook(self, bookName):
        if bookName in self.books:
            print(
                f"You have issued {bookName}. Please keep it safe and do not tear pages of the book and return it in 15 days otherwise the you have to pay the \napplicable charges")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry, The book which you asked for is either not available or has already been issued to someone else and it's not avaiable in library at this point of time. Please wait untill the book is returned")
            return False

    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanks for returning this book! Hope you enjoyed reading this book, Visit again for more books.")


class Student:
    def requestBook(self):
        self.books = input("Enter the name of the book you want to borrow: ")
        return self.books

    def returnBook(self):
        self.books = input("Enter the name of the book you want to return/Donate: ")
        return self.books


if __name__ == "__main__":
    amodLibrary = Library(
        ["Algorithms", "Django", "80/20 Rule", "Atomic Habits", "Python Notes"])
    student = Student()
    while(True):
        welcomeMsg = '''
        **** Welcome to amod's Library ****
        Please choose an option:
        1. List the available books
        2. Request a book
        3. Return/Donate a book
        4. Exit the library
        '''
        print(welcomeMsg)

        Choice = int(input("Enter a choice: "))
        if Choice == 1:
            amodLibrary.displayBooks()
        elif Choice == 2:
            amodLibrary.borrowBook(Student.requestBook(student))
        elif Choice == 3:
            amodLibrary.returnBook(Student.returnBook(student))
        elif Choice == 4:
            print("Thanks for choosing amodLibrary.")
            exit()
        else:
            print("Invalid Choice")