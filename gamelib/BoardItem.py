from gamelib.HacExceptions import HacException, HacInvalidTypeException

class BoardItem():
    """
    Base class for any item that will be placed on a Board.
    Arguments:
    type = str
    name = str
    pos = [x,y]
    model = str
    """
    
    def __init__(self,**kwargs):
        self.name = 'Board item'
        self.type = 'item'
        self.pos = [None,None]
        self.model = '*'
        # Setting class parameters
        for item in ['name','type','pos','model']:
            if item in kwargs:
                setattr(self,item,kwargs[item])

    def __str__(self):
        return self.model
    
    def __repr__(self):
        return self.model
    
    def display(self):
        """
        Print the model WITHOUT carriage return.
        """
        print(self.model,end='')
    
    def debug_info(self):
        """
        Return a string with the list of the attributes and their current value.
        """
        string = "attrs: \n"
        for key in vars(self):
            if type(getattr(self,key)) is list:
                string += f"'{key}' = '"+ ''.join( str(e)+' ' for e in getattr(self,key)) + "'\n"
            else:
                string += f"'{key}' = '" + getattr(self,key) + "'\n"
        return string

    
    def store_position(self,x,y):
        self.pos = [x,y]
    
    def can_move(self):
        """
        This is a virtual method that must be implemented in deriving classes.
        This method has to return True or False.
        This represent the capacity for a BoardItem to be moved by the Board.
        """
        pass



    