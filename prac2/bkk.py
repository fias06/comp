class Book:
    def __init__(self, title, author, genre, price):
        self.title = title
        self.author = author
        self.genre = genre
        self.price = price
        
    def __str__(self):
        return str(self.title) + ", "+str(self.author) +", $"+str(self.price)
    
    def on_sale(self):
        self.price  = round(self.price/2,2)
        
    def is_cheaper(self, other_book):
        if self.price > other_book.price:
            return False
        else:
            return True
        

        