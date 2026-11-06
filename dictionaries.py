# Shopping Cart System with Dictionaries
# AI Engineering - AM


import datetime # module used to get the current date for the receipt


# DICTIONARIES
products = { # inventory: product name & price
   "Boba Tea": 5.50, # product 1
   "Cookie": 2.25, # product 2
   "Sandwich": 7.00, # product 3
   "Chips": 1.75, # product 4
   "Smoothie": 6.25 # product 5
}
shopping_cart = {}


# FUNCTIONS
def money(amount): # turns a number into text like $2.50 (two decimal places)
   total_cents = int(amount * 100 + 0.5) # change dollars to whole cents, rounding up halves
   dollars = total_cents // 100
   cents = total_cents % 100
   if cents < 10: # a single digit needs a zero in front
       cents_text = "0" + str(cents)
   else:
       cents_text = str(cents) # just turn it into text
   return "$" + str(dollars) + "." + cents_text # put the pieces together




def display_products(): # shows all store products
   print() 
   print("----------AVAILABLE PRODUCTS---------- ")
   print() 
   number = 1 # counter to number the products
   for name, price in products.items(): # loop through every product and price
       print(str(number) + ". " + name + " - " + money(price)) # show number, name, price
       number += 1 # move to the next number




def get_valid_number(prompt, low, high): # asks until the number is between low and high
   choice = int(input(prompt)) # get the first answer
   while choice < low or choice > high: # repeat while the answer is out of range
       print("Invalid. Enter a number from", low, "to", high)
       choice = int(input(prompt))
   return choice # give back the valid number




def add_product(cart, store): # adds a product and quantity to the cart
   display_products() # show the products first
   product_names = list(store.keys()) # list so a number matches a name
   print() 
   number = get_valid_number("Enter product number: ", 1, len(product_names)) # validate selection
   name = product_names[number - 1] # find the product name from the number
   quantity = int(input("How many " + name + " would you like to add? ")) # ask for quantity
   while quantity <= 0: # quantity must be greater than 0
       print("Quantity must be greater than 0.")
       quantity = int(input("How many " + name + " would you like to add? ")) # ask again
   if name in cart: # product already in cart
       cart[name] = cart[name] + quantity # add to the existing quantity
   else: # product is new to the cart
       cart[name] = quantity # create a new entry
   print("Added", quantity, name, "to your cart!") # confirmation
   print(name, "quantity is now", cart[name]) # show new quantity




def remove_product(cart): # removes one unit of a product from the cart
   if len(cart) == 0: # check for an empty cart
       print() 
       print("Your cart is empty.")
       return
   print() 
   print("----------YOUR SHOPPING CART----------")
   print() 
   cart_names = list(cart.keys()) # list so a number matches a name
   number = 1 # counter for numbering
   for name in cart_names: # loop through products in the cart
       print(str(number) + ". " + name + " - Quantity: " + str(cart[name])) # show item and quantity
       number += 1
   print() 
   choice = get_valid_number("Enter item number to remove: ", 1, len(cart_names)) # validate
   name = cart_names[choice - 1] # find the product name
   cart[name] = cart[name] - 1 # remove one unit
   print("Removed 1", name, "from your cart!") # confirmation
   if cart[name] == 0: # quantity reached 0
       del cart[name] # delete the key-value pair
       print(name, "was removed from your cart.") # tell the customer
   else:
       print(name, "quantity is now", cart[name]) # show new quantity




def calculate_total_items(cart):  # adds up all quantities
   total = 0  # running total
   for quantity in cart.values():  # loop through each quantity
       total += quantity  # add it
   return total  # return the total number of items




def calculate_subtotal(cart, store):  # price x quantity for each item
   subtotal = 0  # running subtotal
   for name, quantity in cart.items():  # loop through cart items
       subtotal += store[name] * quantity  # add the line total
   return subtotal  # return the subtotal




def calculate_discount(subtotal):  # returns the discount rate for a subtotal
   if subtotal >= 40:  # $40 or more
       return 0.15  # 15%
   elif subtotal >= 20: # $20 to less than $40
       return 0.10  # 10%
   elif subtotal >= 10: # $10 to less than $20
       return 0.05 # 5%
   else: # less than $10
       return 0.0 # no discount




def display_cart(cart, store): # shows the cart with prices and totals
   if len(cart) == 0: # empty cart check
       print() 
       print("Your cart is empty.")
       return # go back to the menu
   print() 
   print("----------YOUR SHOPPING CART----------")
   print() 
   print("Product | Unit Price | Quantity | Line Total")
   number = 1 # counter for numbering
   for name, quantity in cart.items(): # loop through cart items
       price = store[name] # get the price from the products dictionary
       line_total = price * quantity # price x quantity
       print(str(number) + ". " + name + " | " + money(price) + " | " + str(quantity) + " | " + money(line_total)) # row
       number += 1
   print() 
   print("Total Items:", calculate_total_items(cart))  # total items
   print("Subtotal:", money(calculate_subtotal(cart, store)))  # subtotal




def print_receipt(cart, store):  # prints the final receipt
   today = datetime.date.today()  # get the current date
   date_text = str(today.month) + "/" + str(today.day) + "/" + str(today.year)  # month/day/year
   subtotal = calculate_subtotal(cart, store)  # subtotal
   rate = calculate_discount(subtotal)  # discount rate
   saved = subtotal * rate  # amount saved
   final_total = subtotal - saved  # final total
   print() 
   print("----------RECEIPT----------")
   print("Date:", date_text)  # show the date
   print() 
   print("Product | Unit Price | Quantity | Line Total") 
   for name, quantity in cart.items():  # loop through cart items
       price = store[name] # get the price
       line_total = price * quantity
       print(name + " | " + money(price) + " | " + str(quantity) + " | " + money(line_total))  # row
   print() 
   print("Total Items:", calculate_total_items(cart))  # total items
   print("Subtotal:", money(subtotal)) # subtotal
   print("Discount:", str(int(rate * 100)) + "%") # discount percent
   print("Amount Saved:", money(saved)) # amount saved
   print("Final Total:", money(final_total)) # final total
   print() 
   print("Thank you for shopping!") 




# MAIN PROGRAM
def main(): # runs the menu
   running = True # keeps the menu going
   while running: # repeat until successful checkout
       print() 
       print("----------SMART SHOPPING CART----------") 
       print() 
       print("1. View Available Products") 
       print("2. Add Product to Cart") 
       print("3. Remove Product from Cart") 
       print("4. View Shopping Cart") 
       print("5. View Current Total") 
       print("6. Checkout") 
       print() 
       choice = get_valid_number("Enter your choice: ", 1, 6) # validate menu choice
       if choice == 1: # view products
           display_products() # show them
       elif choice == 2: # add product
           add_product(shopping_cart, products) # add to cart
       elif choice == 3: # remove product
           remove_product(shopping_cart) # remove one unit
       elif choice == 4: # view cart
           display_cart(shopping_cart, products) # show cart
       elif choice == 5: # current total
           print() 
           print("Current Subtotal:", money(calculate_subtotal(shopping_cart, products))) # show subtotal
       elif choice == 6: # checkout
           if len(shopping_cart) == 0: # empty cart cannot check out
               print() 
               print("Your cart is empty. Add something before checkout.")
           else:  # cart has items
               print_receipt(shopping_cart, products) # show receipt
               running = False # end the program




main()  # start the program