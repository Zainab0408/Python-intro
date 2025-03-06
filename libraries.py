class library:

    def __init__(self, list_of_books, name):
        self.bookslist=list_of_books
        self.name=name
        self.lendDict={}
    def displaybooks(self):
        print(f"We have the following books in our library: {self.name}")
        for book in self.bookslist:
            print(book)
    def lendbook(self, user, book):
        if book not in self.bookslist:
            print("sorry, we don't have that book.")
        elif book in self.lendDict:
            print("The book is already being used by someone.")
        else:
            self.lendDict[book]=user
            print("You can take the book now.")
        def addBook(self, book):
            self.bookslist.append(book)
            print(f"{book} has been added to the books list")
        def returnBook(self, book):
            if book in self.lendDict:
                del self.lendDict[book]
                print("The book has been returned.")
            else:
                print("that book wasn't borrowed from us.")
if __name__ == '__main__':
    books=library([
        'Five survive', 'How to make friends with the dark', 'to kill a mockingbird', 'anne of greengables'
    ], "let's upskill")
    user_name=input("Welcome to our library!please enter your name:")
