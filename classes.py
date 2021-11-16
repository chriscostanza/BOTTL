class Bottle():
    '''
    Parent class for bottles; liquor, liqueur, wine, soda, etc
    Not used alone
    '''

    def __init__(self,name='',price=0,size=0,stock=0):
        self.name = name #name of bottle
        self.price = price #price of bottle
        self.size = size #size/volume of bottle in millileters
        self.stock = stock #current stock of item

    def __str__(self):
        
        return self.name

    def ppo(self):

        '''
        returns price per fluid ounce (converted from ml)
        '''

        return self.price/(self.size/29.5735)
    
    def total_oz(self):
        
        '''
        Returns total ounces of available liquid based off of bottle size and current stock
        '''
        
        return self.stock * (self.size/29.5735)
    


    
class Liquor(Bottle):

    '''
    Liquor bottle class. Inherits all Bottle attributes and functions
    '''
    
    def __init__(self,name='',price=0,size=0,stock=0,abv=0,spirit=''):
        super().__init__(name='',price=0,size=0,stock=0)
        self.name = name # name of bottle
        self.price = price #p rice of bottle
        self.size = size # size/volume of bottle in millileters
        self.stock = stock #current stock of item
        self.abv = abv # alcohol by volume perecntage
        self.spirit = spirit # Specific type of spirit
        
        
    def info(self):
        '''
        Prints info for bottle including name, price, bottle volume, price per ounce, and current stock
        Liquor specific also prints ABV and spirit type
        '''
        print(f"--- {self.name} ---")
        print("LIQUOR")
        print(f"Spirit: {self.spirit}")
        print(f"ABV: {self.abv} %")
        print(f"Price: {self.price}")
        print(f"Bottle Volume: {self.size} ml")
        print(f"Price Per Ounce: {self.ppo()}")
        print(f"Current Stock : {self.stock}")
        
class Cordial(Bottle):

    '''
    Cordial bottle class. Inherits all Bottle attributes and functions
    '''
    
    def __init__(self,name='',price=0,size=0,stock=0,abv=0):
        super().__init__(name='',price=0,size=0,stock=0)
        self.name = name #name of bottle
        self.price = price #price of bottle
        self.size = size #size/volume of bottle in millileters
        self.stock = stock #current stock of item
        self.abv = abv # alcohol by volume perecntage
        
    def info(self):
        '''
        Prints info for bottle including name, price, bottle volume, price per ounce, and current stock
        Cordial specific also prints ABV
        '''
        print(f"--- {self.name} ---")
        print("CORDIAL")
        print(f"ABV: {self.abv} %")
        print(f"Price: {self.price}")
        print(f"Bottle Volume: {self.size} ml")
        print(f"Price Per Ounce: {self.ppo()}")
        print(f"Current Stock : {self.stock}")
        
class Wine(Bottle):
    
    '''
    Wine bottle class. Inherits all bottle attributes and functions.
    '''
    
    def __init__(self,name='',price=0,size=0,stock=0,abv=0):
        super().__init__(name='',price=0,size=0,stock=0)
        self.name = name #name of bottle
        self.price = price #price of bottle
        self.size = size #size/volume of bottle in millileters
        self.stock = stock #current stock of item
        self.abv = abv # alcohol by volume percentage
        
    def info(self):
        
        '''
        Prints info for bottle including name, price, bottle volume, price per ounce, and current stock
        Wine specific also prints ABV and spirit type
        '''
        print(f"--- {self.name} ---")
        print("WINE")
        print(f"ABV: {self.abv} %")
        print(f"Price: {self.price}")
        print(f"Bottle Volume: {self.size} ml")
        print(f"Price Per Ounce: {self.ppo()}")
        print(f"Current Stock : {self.stock}")
        
class Juice(Bottle):

    '''
    Juice bottle class. Inherits all bottle attributes and functions.
    '''
    
    def info(self):

        '''
        Prints info for bottle including name, price, bottle volume, price per ounce, and current stock
        '''

        print(f"--- {self.name} ---")
        print("JUICE")
        print(f"Price: {self.price}")
        print(f"Bottle Volume: {self.size} ml")
        print(f"Price Per Ounce: {self.ppo()}")
        print(f"Current Stock : {self.stock}")
        
    
class Syrup(Bottle):

    '''
    Wine bottle class. Inherits all bottle attributes and functions.
    '''
    
    def info(self):
        
        '''
        Prints info for bottle including name, price, bottle volume, price per ounce, and current stock
        '''
        print(f"--- {self.name} ---")
        print("SYRUP")
        print(f"Price: {self.price}")
        print(f"Bottle Volume: {self.size} ml")
        print(f"Price Per Ounce: {self.ppo()}")
        print(f"Current Stock : {self.stock}")
        
class Misc(Bottle):

    '''
    Wine bottle class. Inherits all bottle attributes and functions.
    '''

    def info(self):
        
        '''
        Prints info for bottle including name, price, bottle volume, price per ounce, and current stock
        '''
        print(f"--- {self.name} ---")
        print("MISC")
        print(f"Price: {self.price}")
        print(f"Bottle Volume: {self.size} ml")
        print(f"Price Per Ounce: {self.ppo()}")
        print(f"Current Stock : {self.stock}")
    
    
    

class Drink():

    def __init__(self,name='',ingredients=[],garnish=[]):
        self.name = name
        self.ingredients = ingredients
        self.garnish = garnish
        
    def recipe(self):
        
        '''
        Prints complete drink recipe with name, ingredients, and garnishes
        '''
        
        # Prints drink name followed by ingredients and amounts on separate lines
        
        print(f"--{self.name}--")
        for ingr, oz in self.ingredients:
            print(f"{oz} oz of {ingr.name}")
        
        # Concatenates list of garnishes to print at end of recipe
        # If there are no garnishes, it prints nothing
        
        garnish_list = ''
        
        for garn in self.garnish:
            if garn != self.garnish[-1]:
                garnish_list += garn.name +' and '
            else:
                garnish_list += garn.name
        
        if len(garnish_list) > 0:
            print(f'Garnish with {garnish_list}')
        else:
            pass
            

    def cost(self):
        
        '''
        Calculates total rounded cost of drink by iterating through 
        lists of ingredients and garnishes 

        '''

        total = 0

        for ingr,oz in self.ingredients:
            total += ingr.ppo()*oz
        for garn in self.garnish:
            total += garn.pps()

        return round(total,2)

    def retail(self):
        '''
        Calculates retail price based off of percentages. Rounds up.
        '''
        price = round((self.cost()*3),0)

        return price
    
    def total_servings(self,storage):

        '''
        Calculates the total amount of servings based 
        off of the lowest stock ingredient of the drink
        '''
        
        lowest_stock = 100000000000000
        
        for ingr,oz in self.ingredients:
            total_servings = ingr.total_oz()//oz
            if total_servings < lowest_stock:
                lowest_stock = total_servings
        for garn in self.garnish:
            if garn.total_servings() < lowest_stock:
                lowest_stock = garn.total_servings()
                
        return lowest_stock
                

    def info(self):

        '''
        Prints recipe of drink as well as pricing info
        '''
        
        self.recipe()
        print("-------------")
        print(f"Total Cost: {self.cost()}")
        print(f"Suggested Retail: {self.retail()}")
        print(f"Total Profit Per Unit: {self.retail() - self.cost()}")

class Garnish():

    '''
    Object type used for garnishes, i.e. lemon peel, cherry, mint
    '''
    
    def __init__(self,name='',price=0,servings=0,stock=0):
        self.name = name
        self.price = price
        self.servings = servings
        self.stock = stock
        
    def __str__(self):
        
        return self.name
    
    def pps(self):

        '''
        Returns the price per serving based off of serving amount and price per unit
        '''
        
        return self.price/self.servings
    
    def total_servings(self):

        '''
        Returns total number of servings based off of stock and servings per unit
        '''
        
        return self.stock * self.servings
    
    def info(self):

        '''
        Prints name, price, servings per unit, price per serving, and current stock
        '''

        print(f"--{self.name}--")
        print(f"Price: {self.price}")
        print(f"Servings Per Item: {self.servings}")
        print(f"Price Per Serving: {self.pps()}")
        print(f"Current Stock: {self.stock}")