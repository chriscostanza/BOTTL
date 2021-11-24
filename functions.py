from classes import Bottle, Liquor, Cordial, Wine, Juice, Syrup, Misc, Garnish, Drink



def nav_input():

    '''
    Generic input function for menu navigation.
    Converts input into string and returns it
    '''
    
    nav = str(input("Use numbers to navigate the menu: "))
    
    return nav


def main_menu():

    '''
    Text based GUI for Main menu
    '''
    
    print("*******************************")
    print("      --- B O T T L ---")
    print("*******************************")
    print("1) Inventory")
    print("2) Drinks")
    print("3) Add Items")
    print("4) Exit & Save")


def drink_sub_menu():

    '''
    Text based GUI for Drink sub menu
    '''
    
    print("*******************************")
    print("1) Get Drink Info")
    print("2) Delete Item")
    print("3) Go back")
    print("*******************************")
    
        
def item_sub_menu():
    
    '''
    Text based GUI for Item sub menu
    '''

    print("*******************************")
    print("1) View Inventory")
    print("2) Search/Edit Items")
    print("3) Delete Item")
    print("4) Go back")
    print("*******************************")
    
def create_sub_menu():

    '''
    Text based GUI for Create item/drink sub menu
    '''
    
    print("*******************************")
    print("1) New Bottle")
    print("2) New Garnish")
    print("3) New Drink")
    print("4) Go back")
    print("*******************************")


def general_search(storage):

    '''
    Search function. Takes in list to iterate through and find an item based off of
    the .name() function that belongs to all classes. 
    You can type 'back' at any time and the func returns False boolean.
    '''

    while True:
        search_term = input("What are you looking for? Type back if you'd like to go back.")

        if search_term.lower() == 'back':
            return False
        else:

            results = [x for x in storage if search_term.lower() in x.name.lower()]

            if len(results) == 0:
                print("Nothing found that matches your search! Try again or type back to go back. ")
            else:
                print("*******************************")
                print(f"-- Number of Search Results: {len(results)} --")
                print("*******************************")
                for item in results:
                    print(item.name)
                    return results

def item_select(results):

    '''
    Used to select and return a specific item from a list. Usually used in conjunction
    with the general_search function.
    You can type 'back' at any time and the func returns False boolean.
    '''
    
    while True:
        answer = input("Type which item you'd like to select'. Type back if you'd like to go back.")
        
        if answer.lower() == 'back':
            return False
        else:   
            for item in results:
                if answer.lower() in item.name.lower():
                    return item
            else:
                print("Item not found, try again.")



def list_inventory(storage):
    
    '''
    Prints list for items in inventory.
    Allows user to Choose which specific type of
    item they would like to view or view all.
    '''
    
    # Lists of specific classes for specific printing

    liquors = list(filter(lambda x: isinstance(x,Liquor),storage))
    cordials = list(filter(lambda x: isinstance(x,Cordial),storage))
    wines = list(filter(lambda x: isinstance(x,Wine),storage))
    juices = list(filter(lambda x: isinstance(x,Juice),storage))
    syrups = list(filter(lambda x: isinstance(x,Syrup),storage))
    misc = list(filter(lambda x: isinstance(x,Misc),storage))
    garnishes = list(filter(lambda x: isinstance(x,Garnish),storage))
    

    # List of viewing options
    while True:

        print("1) Liquor")
        print("2) Cordials")
        print("3) Wines")
        print("4) Juices")
        print("5) Misc")
        print("6) Garnishes")
        print("7) View All")
        print("8) Back")

        # User input
        viewing = str(input("What would you like to view?"))
        
        # List liquors
        if viewing == '1':
            print("*******************************")
            print("     --- L I Q U O R ---")
            print("*******************************")
            for item in liquors:
                print(f">>> {item}")
            print("\n")
        
        # List Cordials
        if viewing == '2':
            print("*******************************")
            print("    --- C O R D I A L S ---")
            print("*******************************")
            for item in cordials:
                print(f">>> {item}")
            print("\n")
        
        # List Wines    
        if viewing == '3':
            print("*******************************")
            print("      --- W I N E S ---")
            print("*******************************")
            for item in wines:
                print(f">>> {item}")
            print("\n")
        
        # List Juices   
        if viewing == '4':
            print("*******************************")
            print("     --- J U I C E S ---")
            print("*******************************")
            for item in juices:
                print(f">>> {item}")
            print("\n")
        
        # List Misc   
        if viewing == '5':
            print("*******************************")
            print("       --- M I S C ---")
            print("*******************************")
            for item in misc:
                print(f">>> {item}")
            print("\n")
        
        # List Garnishes   
        if viewing == '6':
            print("*******************************")    
            print("   --- G A R N I S H E S ---")
            print("*******************************")
            for item in garnishes:
                print(f">>> {item}")
        
        # List all items in inventory     
        if viewing == '7':
    
            print("*******************************")
            print("     --- L I Q U O R ---")
            print("*******************************")
            for item in liquors:
                print(f">>> {item}")
            print("\n")
            print("*******************************")
            print("    --- C O R D I A L S ---")
            print("*******************************")
            for item in cordials:
                print(f">>> {item}")
            print("\n")
            print("*******************************")
            print("      --- W I N E S ---")
            print("*******************************")
            for item in wines:
                print(f">>> {item}")
            print("\n")
            print("*******************************")
            print("     --- J U I C E S ---")
            print("*******************************")
            for item in juices:
                print(f">>> {item}")
            print("\n")
            print("*******************************")
            print("       --- M I S C ---")
            print("*******************************")
            for item in misc:
                print(f">>> {item}")
            print("\n")
            print("*******************************")    
            print("   --- G A R N I S H E S ---")
            print("*******************************")
            for item in garnishes:
                print(f">>> {item}")
            print("\n")
        
        # Back command
        if viewing == '8':
            return False

        

def list_menu(menu):

    '''
    Lists all drinks and their recipes.
    Takes in list used to store the drink class objects.
    '''
    
    print("*******************************")
    print("      --- D R I N K S ---")
    print("*******************************")
    for item in menu:
        item.recipe()
        print("*******************************")



def create_bottle(storage):

    '''
    Used to create a new bottle object. 
    Takes in list where the object will be stored.
    Saves appended list via pickle after creation
    '''
    
    def save_storage():

        '''
        imports pickle and saves list
        '''

        import pickle

        with open('storage.pickle','wb') as write_storage:
            pickle.dump(storage,write_storage)

    
    # Bottle Type Selection
    while True:
        print("1) Liquor")
        print("2) Coridal/Liqueur")
        print("3) Wine")
        print("4) Juice")
        print("5) Syrup")
        print("6) Misc")
        print("7) Back")

        # User input for bottle type
        bottle_type = str(input('What type of bottle is this?'))
        
        if bottle_type in ['1','2','3','4','5','6']:
            break
        
        # Back function returns false boolean
        elif bottle_type == '7':
            return False
        
        else:
            print("Invalid input. Use numbers to choose your action")
        
    
    # User input to name object
    name = str(input("Enter the name of the bottle: "))
    

    # User inputs various univeral bottle attributes applicable to all sub classes
    
    # Bottle price input loop
    while True:
        try:
            price = float(input("Please enter the price of the bottle in USD: "))
            break
        except ValueError:
            print("Not a valid price. Please use intergers.")
    
    # Bottle size / volume input loop
    while True:
        try:
            size = int(input("Please enter the size/volume of the bottle in ml: "))
            break
        except ValueError:
            print("Not a valid size/volume. Please use intergers.")
    
    # Bottle stock input loop
    while True:
        try:
            stock = int(input("Please enter the current stock of the bottle: "))
            break
        except ValueError:
            print("Not a valid stock number. Please use intergers.")
            
    

    # Liquor specific info input
    if bottle_type == '1':
        
        # Spirit type selection menu
        while True:
            
            # List of possible spirit type names
            spiritlist = ['','Whiskey','Gin','Tequila/Mezcal','Rum','Vodka','Other']
            print("1) Whiskey")
            print("2) Gin")
            print("3) Tequila/Mezcal")
            print("4) Rum")
            print("5) Vodka")
            print("6) Other")
            
            # User input to select spirit. 
            try:
                
                spirit_choice = int(input('What type of spirit is this?'))
                
                if spirit_choice not in range(1,7):
                    print("Not a valid number")
                    continue
                
                # Uses user input to assign selected spirit type from list
                else:
                    spirit = spiritlist[spirit_choice]
                    break
            
            except ValueError:
                print("Invalid input. Use numbers to choose your action")
                     

        # ABV input
        while True:
            try:
                abv = float(input("Please enter the alcohol by volume % of the bottle: "))
                break
            except ValueError:
                print("Not a valid amount. Please use intergers.")
                
        # Creating new object and appending list
        # Saves list to pickle document and prints name and stock
        # Returns False boolean to end function
        storage.append(Liquor(name,price,size,stock,abv,spirit))
        save_storage()
        print(f"Added {name} to inventory.")
        print(f"Current Stock: {stock}")
        return False

    
    # Cordial specific input
    if bottle_type == '2':
        
        # ABV input
        while True:
            try:
                abv = float(input("Please enter the alcohol by volume % of the bottle: "))   
                break
            except ValueError:
                print("Not a valid amount. Please use intergers.")
        
        # Creating new object and appending list
        # Saves list to pickle document and prints name and stock
        # Returns False boolean to end function
        storage.append(Cordial(name,price,size,stock,abv))
        save_storage()
        print(f"Added {name} to inventory.")
        print(f"Current Stock: {stock}")
        return False
        
            
    # Wine specific input
    if bottle_type == '3':
        
        # ABV input
        while True:
            try:
                abv = float(input("Please enter the alcohol by volume % of the bottle: "))
                break
            except ValueError:
                print("Not a valid amount. Please use intergers.")
        
        # Creating new object and appending list
        # Saves list to pickle document and prints name and stock
        # Returns False boolean to end function               
        storage.append(Wine(name,price,size,stock,abv))
        save_storage()
        print(f"Added {name} to inventory.")
        print(f"Current Stock: {stock}") 
        return False
        
    
    # Juice bottle create
    if bottle_type == '4':

        # Creating new object and appending list
        # Saves list to pickle document and prints name and stock
        # Returns False boolean to end function
        storage.append(Juice(name,price,size,stock))
        save_storage()
        print(f"Added {name} to inventory.")
        print(f"Current Stock: {stock}")       
        return False
    
    
    # Syrup bottle create
    if bottle_type == '5':
        # Creating new object and appending list
        # Saves list to pickle document and prints name and stock
        # Returns False boolean to end function
        storage.append(Syrup(name,price,size,stock))
        save_storage()
        print(f"Added {name} to inventory.")
        print(f"Current Stock: {stock}")        
        return False
    
    
    # Misc bottle create
    if bottle_type == '6':
        # Creating new object and appending list
        # Saves list to pickle document and prints name and stock
        # Returns False boolean to end function
        storage.append(Misc(name,price,size,stock))
        save_storage()
        print(f"Added {name} to inventory.")
        print(f"Current Stock: {stock}")
        return False

    
    
    
    
def create_garnish(storage):

    '''
    Used to create a new garnish object. 
    Takes in list where the object will be stored.
    Saves appended list via pickle after creation
    '''

    def save_storage():

        '''
        imports pickle and saves list
        '''
        import pickle
        
        with open('storage.pickle','wb') as write_storage:
            pickle.dump(storage,write_storage)

    
    # User inputs name of garnish
    name = str(input("Enter the name of the garnish: "))
    

    # Price input
    while True:
        try:
            price = float(input("Please enter the price of the garnish in USD: "))
            break
        except ValueError:
            print("Not a valid price. Please use intergers.")
    
    
    # Servings input
    while True:
        try:
            servings = int(input("Please enter the number of servings per item/container: "))
            break
        except ValueError:
            print("Not a valid amount. Please use intergers.")
    

    # Stock input
    while True:
        try:
            stock = int(input("Please enter the current stock of the garnish: "))
            break
        except ValueError:
            print("Not a valid stock number. Please use intergers.")
        
    
    # Creating new object and appending list
    # Saves list to pickle document and prints name and stock
    # Returns False boolean to end function
    storage.append(Garnish(name,price,servings,stock))
    save_storage()
    print(f"Added {name} to inventory.")
    print(f"Current Stock: {stock}")
    return False
    

    
def create_drink(menu,storage):

    '''
    Used to create a new Drink object. 
    Takes in list where the object will be stored.
    Saves appended list via pickle after creation
    '''

    def save_menu():

        '''
        imports pickle and saves list
        '''

        import pickle
        
        with open('menu.pickle','wb') as write_menu:
            pickle.dump(menu,write_menu)

    def add_amount(item):

          while True:
            try:
                amount = float(input("How many ounces?"))
                ingredients.append((item,amount))
                print(f"Added {amount} ounces of {item.name} to {name}.")
                print("*******************************")
                break
            except ValueError:
                print("Not a valid amount, try again.")


    # Creating lists of bottle and garnishes to be referenced later
    bottles_list = list(filter(lambda x: isinstance(x,Bottle),storage))
    garnishes_list = list(filter(lambda x: isinstance(x,Garnish),storage))


    # User input for name of Drink
    name = str(input("Enter the name of the drink: "))

    # Creating lists for ingredients and garnishes of the drink
    ingredients = []
    garnish = []
    
    # Back function
    if name == 'back':
        return False
    else:
        pass
    

    enter_ingr = True
    enter_garnish = True
    
    # Enter ingredient begins
    while enter_ingr:
        
        # Takes user input and compiles list of matching results
        ingr_search = str(input("Enter the name of the ingredient you wish to add. Type 'Done' if you are done adding ingredients: "))
        results = [x for x in bottles_list if ingr_search.lower() in x.name.lower()]
        
        # back
        if ingr_search.lower() == 'done':
            enter_ingr = False

        # No results returned
        elif len(results) == 0:
            print("Nothing found that matches your search! Try again or type back to go back. ")
            continue
        
        # One result returned 
        elif len(results) == 1:
            while True:
                
                add_ask = str(input(f"Did you want to add {results[0].name}? "))

                if add_ask[0].lower() == 'n':
                    break
                
                elif add_ask[0].lower() == 'y':
                    print(f"Adding {results[0].name}")
                    add_amount(results[0])
                    break

        # More than one result returned
        else:
            print("*******************************")
            for item in results:
                print(item.name)
            print("*******************************")
            
            # User selects item to add from search results    
            ingr = str(input("Which bottle did you want to add? "))
 
            for item in results:
                if ingr.lower() == item.name.lower():
                    print(f"Adding {item.name}")
                    add_amount(item)
                    break
                    
                elif ingr.lower() not in item.name.lower():
                    if item == storage[-1]:
                        print("Item not found, try again.")
                    else:
                        pass
    
    # Enter garnish begins
    while enter_garnish:

        # Takes user input and compiles list of matching results
        garn_search = str(input("Enter the name of the garnish you wish to add. Type 'Done' if you are done adding garnishes: "))
        results = [x for x in garnishes_list if garn_search.lower() in x.name.lower()]
        
        # Done adding garnishes
        if garn_search.lower() == 'done':
            break

        # No results returned
        elif len(results) == 0:
            print("Nothing found that matches your search! Try again or type back to go back. ")
            continue

        # One result returned
        elif len(results) == 1:
            while True:
                
                add_ask = str(input(f"Did you want to add {results[0].name}? "))

                if add_ask[0].lower() == 'n':
                    break
                elif add_ask[0].lower() == 'y':
                    print(f"Adding {results[0].name}")
                    break
        
        # More than one result returned
        else:
            print("*******************************")
            for item in results:
                print(item.name)
            print("*******************************")
            
            # User selects item to add from search results 
            garn = str(input("Which garnish did you want to add? "))
            
            # Iterate through garnish list to find match and add it
            for item in results:
                
                if garn.lower() == item.name.lower():
                    print(f"Adding {item.name}")
                    print("*******************************")
                    garnish.append(item)
                    break

                elif garn.lower() not in item.name.lower():
                    if item == results[-1]:
                        print("Garnish not found, try again.")
                        print("*******************************")
                    else:
                        pass
    
    print(f"{name} created!")
    menu.append(Drink(name,ingredients,garnish))
    save_menu()
    return False



def delete_item(storage,menu):
    
    '''
    Deletes an item from a list. Can be used for any type of object.
    storage = list containing item to be deleted
    menu = list of drink recipes
    Checks if item is being used in any drinks.
    If it is being used, it doesn't allow user to delete item and notifies the user.
    '''
    
    del_commence = False
    
    # Start delete search sequence
    while True:
        # Setting variable to keep track of list index 
        current_index = 0
        # User input to search for item to be deleted
        del_item = str(input("What would you like to delete? Type 'back' if you'd like to go back. "))

        # Back
        if del_item.lower() == 'back':
            return False
        # Iterate through storage
        else:
            for item in storage:
                # Item found in storage, commence next check
                if del_item.lower() in item.name.lower():
                    del_item = storage[current_index]
                    del_commence = True
                    break
                # Checks if it is on last item in list. If item not found, print error and go back
                elif item == storage[-1]:
                    print("Item not found! Try again.")
                    break
                
                # Add to index variable to keep track of current index
                else:
                    current_index += 1 
        

        while del_commence == True:
            # Iterate through menu items to check if ingredient is in use 
            for drink in menu:
                # Ingredient or garnish is being used in drink notify user and break out of deletion
                if del_item.name in list(x.name for x,y in drink.ingredients) or del_item.name in list(x.name for x in drink.garnish):
                    print(f"{del_item.name} is currently being used in a drink!")
                    print("Please delete all drinks containg this item.")
                    del_commence = False
                    break
                # Item not found in a drink, continue to user confirmation
                else:
                    pass
            # Confirm item deletion via user input        
            del_ask = str(input(f"Did you want to delete {item.name}? Type yes or no: "))
            # Delete item and notify user
            if del_ask[0].lower() == 'y':
                    deleted = storage.pop(current_index)
                    print(f"{deleted.name} was deleted!")
                    del_commence = False
                    break
            # Notify that item will not be deleted, break out of loop
            else:
                print("Item not deleted.")
                break



def item_edit(item):

    '''
    Used to edit any non drink object
    '''
    # Navigation variable
    nav = '0'
    
    # Overall Function loop
    while True:

        # Menu if item is a bottle object
        while isinstance(item,Bottle):
            while nav == '0':
                print("*******************************")
                print("        --- I N F O ---")
                print("*******************************")
                item.info()
                print("\n")
                print("1) Change Stock")
                print("2) Edit Item")
                print("3) Go Back")
                # User navigation input
                nav = str(input("What would you like to do? "))

            # Change stock
            while nav == '1':
                print(f"{item.name} Current Stock: {item.stock}")
                try:
                    new_stock = int(input("Enter the new stock amount: "))
                    item.stock = new_stock
                    print(f"{item.name} stock updated to {new_stock}!")
                    nav = '0'
                except ValueError:
                    print("Not a valid amount! Try again.")
            
            # Edit item attributes menu
            while nav == '2':
                # Liquor object menu
                while isinstance(item,Liquor):
                    print("1) Name")
                    print("2) Price")
                    print("3) Size")
                    print("4) ABV %")
                    print("5) Spirit")
                    print("6) Go Back")
                    # User navigation variable / input
                    edit_nav = str(input("What would you like to edit?"))
                    # Name edit
                    if edit_nav == '1':
                        new_name = str(input("What would you like to rename this item?"))
                        item.name = new_name
                        print(f"Item renamed {item.name}!")
                        continue
                    # Price edit
                    elif edit_nav == '2':
                        try:
                            new_price = float(input("What is this item's new price? "))
                            item.price = new_price
                            print(f"{item.name}'s new price is {item.price}!")
                            continue
                        except ValueError:
                            print("Not a valid amount.")
                    # Size edit
                    elif edit_nav == '3':
                        try:
                            new_size = float(input("What is this item's new size/volume? "))
                            item.size = new_size
                            print(f"{item.name}'s new size is {item.size} ml!")
                            continue
                        except ValueError:
                            print("Not a valid amount.")
                    # ABV edit
                    elif edit_nav == '4':
                        try:
                            new_abv = float(input("What is this item's new ABV %? "))
                            item.abv = new_abv
                            print(f"{item.name}'s new ABV is {item.abv} %!")
                            continue
                        except ValueError:
                            print("Not a valid amount.")
                    # Spirit type edit
                    elif edit_nav == '5':
                        while True:
                            spiritlist = ['','Whiskey','Gin','Tequila/Mezcal','Rum','Vodka','Other']
                            print("1) Whiskey")
                            print("2) Gin")
                            print("3) Tequila/Mezcal")
                            print("4) Rum")
                            print("5) Vodka")
                            print("6) Other")
                            try:
                                spirit = int(input('What are you changing the spirit type to?'))
                                if spirit not in range(1,7):
                                    print("Not a valid number")
                                    continue
                                else:
                                    item.spirit = spiritlist[spirit]
                                    print(f"{item.name}'s new spirit type is {item.spirit}!'")
                                    break
                            except ValueError:
                                print("Invalid input. Use numbers to choose your action")
                    # Back
                    elif edit_nav == '6':
                        nav = '0'
                        break
                # Wine or Cordial object edit menu
                while isinstance(item,Wine) or isinstance(item,Cordial):
                    print("*******************************")
                    print("        --- I N F O ---")
                    print("*******************************")
                    item.info()
                    print("\n")
                    print("1) Change Stock")
                    print("2) Edit Item")
                    print("3) Go Back")
                    nav = str(input("What would you like to do? "))
                    # Name edit
                    if edit_nav == '1':
                        new_name = str(input("What would you like to rename this item?"))
                        item.name = new_name
                        print(f"Item renamed {item.name}!")
                        continue
                    # Price edit
                    elif edit_nav == '2':
                        try:
                            new_price = float(input("What is this item's new price? "))
                            item.price = new_price
                            print(f"{item.name}'s new price is {item.price}!")
                            continue
                        except ValueError:
                            print("Not a valid amount.")
                    # Size edit
                    elif edit_nav == '3':
                        try:
                            new_size = float(input("What is this item's new size/volume? "))
                            item.size = new_size
                            print(f"{item.name}'s new size is {item.size} ml!")
                            continue
                        except ValueError:
                            print("Not a valid amount.")
                    # ABV Edit
                    elif edit_nav == '4':
                        try:
                            new_abv = float(input("What is this item's new ABV %? "))
                            item.abv = new_abv
                            print(f"{item.name}'s new ABV is {item.abv} %!")
                            continue
                        except ValueError:
                            print("Not a valid amount.")
                    # Back 
                    elif edit_nav == '5':
                        nav = '0'
                        break
                # Juice, syrup, or misc object edit menu      
                while isinstance(item,Juice) or isinstance(item,Syrup) or isinstance(item,Misc):
                    print("*******************************")
                    print("        --- I N F O ---")
                    print("*******************************")
                    item.info()
                    print("\n")
                    print("1) Change Stock")
                    print("2) Edit Item")
                    print("3) Go Back")
                    nav = str(input("What would you like to do? "))
                    # Name edit
                    if edit_nav == '1':
                        new_name = str(input("What would you like to rename this item?"))
                        item.name = new_name
                        print(f"Item renamed {item.name}!")
                        continue
                    # Price edit
                    elif edit_nav == '2':
                        try:
                            new_price = float(input("What is this item's new price? "))
                            item.price = new_price
                            print(f"{item.name}'s new price is {item.price}!")
                            continue
                        except ValueError:
                            print("Not a valid amount.")
                    # Size edit
                    elif edit_nav == '3':
                        try:
                            new_size = float(input("What is this item's new size/volume? "))
                            item.size = new_size
                            print(f"{item.name}'s new size is {item.size} ml!")
                            continue
                        except ValueError:
                            print("Not a valid amount.")

                    # Back
                    elif edit_nav == '4':
                        nav = '0'
                        break

            # Break out of function 
            while nav == '3':
                return False

        # Menu if item is a garnish object
        while isinstance(item,Garnish):
            while nav == '0':
                print("*******************************")
                print("        --- I N F O ---")
                print("*******************************")
                item.info()
                print("\n")
                print("1) Change Stock")
                print("2) Edit Item")
                print("3) Go Back")
                nav = str(input("What would you like to do? "))
            # Stock edit
            while nav == '1':
                print(f"{item.name} Current Stock: {item.stock}")
                try:
                    new_stock = int(input("Enter the new stock amount: "))
                    item.stock = new_stock
                    print(f"{item.name} stock updated to {new_stock}!")
                    nav = '0'
                except ValueError:
                    print("Not a valid amount! Try again.")
            # Edit object attributes menu
            while nav == '2':
                print("1) Name")
                print("2) Price")
                print("3) Servings")
                print("4) Go Back")
                edit_nav = str(input("What would you like to edit?"))
                # Name edit
                if edit_nav == '1':
                    new_name = str(input("What would you like to rename this item?"))
                    item.name = new_name
                    print(f"Item renamed {item.name}!")
                    continue
                # Price Edit
                elif edit_nav == '2':
                    try:
                        new_price = float(input("What is this item's new price? "))
                        item.price = new_price
                        print(f"{item.name}'s new price is {item.price}!")
                        continue
                    except ValueError:
                        print("Not a valid amount.")
                # Servings edit
                elif edit_nav == '3':
                    try:
                        new_servings = float(input("What is this item's new serving amount? "))
                        item.servings = new_servings
                        print(f"{item.name}'s new serving amount is {item.servings}!")
                        continue
                    except ValueError:
                        print("Not a valid amount.")
                # Back
                elif edit_nav == '4':
                    nav = '0'

            while nav == '3':
                return False
