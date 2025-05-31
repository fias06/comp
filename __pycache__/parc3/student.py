class Book:
    def __init__(self, title, author, isbn, available = True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available 
        
    def __str__(self):
        return(str(self.title)+" by "+str(self.author)+" (ISBN: "+str(self.isbn)+")")
        

class Member:
    def __init__(self, name, member_id, borrowed_books = []):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = borrowed_books = []
        
    def __str__(self):
        return str(self.name)
        
    def borrow_book(self, book):
        if book.available == True:
            self.borrowed_books.append(book)
            book.available == False
            print(str(self.name)+" borrowed "+str(book))
        else:
            print("Book not available")      
    
    def return_books(self, book):
        self.borrowed_books.remove(book)
        book.available == True
        print(str(self.name)+" returned "+str(book))
        
    def list_borrowed_books(self):
        for i in self.borrowed_books:
            print(i)
            
class Library:
    def __init__(self, name, books = [], members= []):
        self.name = name
        self.books = books 
        self.members = members 
        
    def add_books(self, book):
        self.books.append(book)
        print("Added book "+str(book))
        
    def register_member(self,member):
        self.members.append(member)
        print("Registered member "+str(member))
        
    def list_available_books(self):
        for i in self.books:
            print(i)
            
    def list_all_members(self):
        for i in self.members:
            print(i)
            

    
my_library = Library("McGill Main Library")

# Create books
book1 = Book("1984", "George Orwell", "9780451524935")
book2 = Book("The Hobbit", "J.R.R. Tolkien", "9780547928227")
book3 = Book("To Kill a Mockingbird", "Harper Lee", "9780061120084")

# Add books to library
my_library.add_books(book1)
my_library.add_books(book2)
my_library.add_books(book3)

# Create members
member1 = Member("Saif Shaikh", 101)
member2 = Member("Jane Doe", 102)

# Register members
my_library.register_member(member1)
my_library.register_member(member2)

# Members borrow books
member1.borrow_book(book1)
member1.borrow_book(book2)
member2.borrow_book(book1)  # Should say not available

# List available books
my_library.list_available_books()

# Member returns a book
member1.return_books(book1)

# Now member2 can borrow it
member2.borrow_book(book1)

# List who has what
member1.list_borrowed_books()
member2.list_borrowed_books()