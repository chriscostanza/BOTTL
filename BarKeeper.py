'''

--- B A R K E E P E R ---

'''


if __name__ == '__main__':

    # Importing classes, functions, and pickle
    
    from classes import Bottle, Liquor, Cordial, Wine, Juice, Syrup, Misc, Garnish, Drink
    import functions as f
    import pickle

    
    # Opening pickled lists. if the pickled list is empty, it avoids the EOF error
    # with the try/except and instead creates an empty list. The list gets perma saved when
    # you add an item to it.
    try:
        with open('storage.pickle','rb') as open_storage:
            storage = pickle.load(open_storage)
    except EOFError:
        storage = []
    except FileNotFoundError:
        storage = []
        with open('storage.pickle','wb') as open_storage:
            pickle.dump(storage,open_storage)
    try:
        with open('menu.pickle','rb') as open_menu:
            menu = pickle.load(open_menu)
    except EOFError:
        menu = []
    except FileNotFoundError:
        menu = []
        with open('menu.pickle','wb') as open_menu:
            pickle.dump(menu,open_menu)

    # Setting main menu navigation variable
    nav = '0'
    # Setting main program run variable
    program_run = True


    while program_run:

        # MAIN MENU
        while nav == '0':
            
            f.main_menu()
            
            while True:

                nav = f.nav_input()

                if nav in list(str(x) for x in range(1,5)):
                    break
                else:
                    print("Not a valid input. Try again.")
                    continue

        # LIQUOR SUB MENU
        while nav == '1':
            
            sub_nav = '0'
            
            # INVENTORY MENU
            while sub_nav == '0':
                
                # Navigation / Input
                f.item_sub_menu()
                sub_nav = f.nav_input()
            
            # VIEW INVENTORY OPTIONS
            while sub_nav == '1':
                
                if f.list_inventory(storage)== False:
                    sub_nav = '0'
                    break
                else:
                    pass

            # SEARCH AND EDIT ITEMS
            while sub_nav == '2':
                
                results = f.general_search(storage)
                if results == False:
                    sub_nav == 0
                    break
                else:
                    pass
                item = f.item_select(results)
                if item == False:
                    sub_nav = '0'
                    break
                else:
                    f.item_edit(item)
            
            # DELETE ITEM
            while sub_nav == '3':
                
                item = f.delete_item(storage,menu)
                if item == False:
                    sub_nav = '0'
            
            # GO BACK
            while sub_nav == '4':
                
                nav = '0'
                break
                    
        # DRINKS SUB MENU            
        while nav == '2':
            
            sub_nav = '0'
            
            # VIEW DRINK RECIPES / USER INPUT
            while sub_nav == '0':
                
                # Navigation / Input
                f.list_menu(menu)
                f.drink_sub_menu()
                sub_nav = f.nav_input()


            # GET SPECIFIC DRINK INFO
            while sub_nav == '1':
                
                # User input
                item = f.item_select(menu)
                
                # Go back
                if item == False:
                    sub_nav = '0'
                    break
                
                # Print all item info as well as total servings availabe
                else:
                    print("*******************************")
                    item.info()
                    print(f"Total Available Servings: {item.total_servings(storage)}")
                    print("*******************************")
            
            # DELETE DRINK
            while sub_nav == '2':
                
                item = f.delete_item(menu,menu)
                
                if item == False:
                    sub_nav = '0'
            
            # GO BACK
            while sub_nav == '3':
                
                nav = '0'
                break
        
        # CREATE NEW ITEM / DRINK SUB MENU                
        while nav == '3':
            
            sub_nav = '0'
            
            # CHOOSE TYPE TO CREATE
            while sub_nav == '0':
                
                # Navigation / Input
                f.create_sub_menu()
                sub_nav = f.nav_input()
            
            # CREATE BOTTLE
            while sub_nav == '1':
                if f.create_bottle(storage) == False:
                    sub_nav = '0'
                    break
                else:
                    continue
            
            # CREATE GARNISH
            while sub_nav == '2':
                if f.create_garnish(storage) == False:
                    sub_nav = '0'
                    break
                else:
                    continue
            
            # CREATE DRINK
            while sub_nav == '3':
                if f.create_drink(menu,storage) == False:
                    sub_nav = '0'
                    break
                else:
                    continue
            
            # GO BACK
            while sub_nav == '4':
                nav = '0'
                break

        # END PROGRAM
        while nav == '4':

            program_run = False
            break

