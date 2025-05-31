class Product:
    
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
        
    def __str__(self):
        return str(self.name) + " for " + str(self.price) + ", " +str(self.stock) + " in stock"
    

class Customer:
    def __init__(self, name, email, cart = []):
        self.name = name
        self.email = email
        self.cart = cart
        
    def add_to_cart(self, product):
        self.cart.append(product)
        print(str(product)+" added to cart")
        
    def remove_from_cart(self, product):
        self.cart.remove(product)
        print(str(product) + " removed from cart")
        
    def place_order(self):
        total = 0
        for i in self.cart:
            total += 1
            i.stock -= 1
            
        new = Order(self.cart, total)
        print("Order created")
        
class Order:
    def __init__(self, products, total_price):
        self.products = products
        self.total_price = total_price
        self.status = "Placed"
        
    def calculate_total(self):
        total = sum(self.price)
        print("The total amount is "+str(total))
        
    def __str__(self):
        return str(self.order_id) + " for " + str(self.products) + ". Price: "+str(self.price)
    
    

   
p1 = Product("Laptop", 1200, 5)
p2 = Product("Headphones", 150, 10)
p3 = Product("Mouse", 25, 0)  # Out of stock

# Create a customer
c1 = Customer("Saif Shaikh", "saif@example.com")

# Customer adds items to cart
c1.add_to_cart(p1)
c1.add_to_cart(p2)
c1.add_to_cart(p3)  # Out of stock, won't be added

# Remove an item
c1.remove_from_cart(p2)

# Add it back again
c1.add_to_cart(p2)

# Place an order
order1 = c1.place_order()

# Print order details
if order1:
    print(order1)

# Try placing another order with an empty cart
c1.place_order()    