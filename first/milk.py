# TODO: Reorganize the following code with the necessary spaces (indentation) and remove any unnecessary lines
# No character per line limitation in this part
# No comment is needed in this part
print("Welcome to the DIY Milktea Maker!")
cup_size = input("Please enter your desired size of cup (Please enter s for small, m for medium, or l for large): ")
temperature_answer = input("Do you want hot milk? (Yes/No): ")
if cup_size == "s":
    cup_volume = "small"
elif cup_size == "m":
    cup_volume = "medium"
elif cup_size == "l":
    cup_volume = "large"

if temperature_answer == "Yes":
    temperature = "hot"
else:
    temperature = "cold"

lactose_choice = input("Do you want lactose free milk? (Yes/No): ")
if lactose_choice == "Yes":
    milk_choice = input("Do you want soy milk or oat milk? (soy/oat): ")
else:
    milk_choice = "regular"

print("Your drink is a", cup_volume, "size,", temperature, "milktea", "with", milk_choice, "milk base")
print("\nEnjoy your drink!\n")    










    
    
