class Book:
    def __init__(self, builder):
        """ constructor """
        self.Name = builder.Name
        self.Author = builder.Author
        self.Year = builder.Year

    def getName(self):
        return self.Name

    def getAuthor(self):
        return self.Author

    def getYear(self):
        return self.Year

    @staticmethod
    def getBuilder():
        return _Builder()

class _Builder:
    """
    Beginning underscore signifies the Builder class is private.
    """
    def Name(self, Name):
        self.Name = Name
        return self

    def Author(self, Author):
        self.Author = Author
        return self

    def Year(self, Year):
        self.Year = Year
        return self

    def build(self):
        return Book(self)

if __name__ == '__main__':
    book = Book.getBuilder().Name("Alchemist").Author("Paulo Coelho").Year(1988).build()
    print(book.getName() + " by " + book.getAuthor() + "\nYear : " + str(book.getYear()))
