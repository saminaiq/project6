#Class Methods
#Assigment:
#Create a class book with a class variable total-books.Add a class method incereement_book_count() to increase the count when a new book is added







class Book:
    total_books = 0  

    def __init__(self):
        Book.increment_books_count()  

    @classmethod
    def increment_books_count(cls):
        cls.total_books += 1  

    @classmethod
    def sum(cls):
        print(f"Total books: {cls.total_books}") 


Book.increment_books_count ()#Ist book
Book.increment_books_count ()#2nd book
Book.increment_books_count ()#3rd book
Book.increment_books_count ()#4th book

# Total books
Book.sum()

#output:
#Total books:4