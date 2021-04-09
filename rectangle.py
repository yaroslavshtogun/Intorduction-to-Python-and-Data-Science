class Rectangle:
    """
    A class used to represent an Rectangle and its properties.

    Attributes
    ----------
    _width : int
        the integer value of the rectangle width (default 1)
    _height : int
        the integer value of the rectangle height (default 1)

    Methods
    -------
    setWidth(width)
        set rectangle width 
        
    setHeight(height)
        set rectangle height 
        
    getWidth()
        get rectangle width 
        
    getHeight()
        get rectangle height         

    area()
        get rectangle area 
        
    perimeter()
        get rectangle perimeter 
        
    __str__()
        print rectangle width anf height 

    """
     
    def __init__(self, width = 1, height = 1):
        """
        Parameters
        ----------
        _width : int
            the integer value of the rectangle width (default 1)
        _height : int
            the integer value of the rectangle height (default 1)
        """          
        self.width = width
        self.height = height
    
    def setWidth(self, width):
        """
        The method sets the width value
        
        Parameters
        ----------
        width : int
            the integer value of the rectangle width 
        
        Return 
        ----------
        None 

        """
           
        self._width = width
        
    def setHeight(self, height):
        """
        The method sets the height value 
        
        Parameters
        ----------
        height : int
            the integer value of the rectangle height 
        
        Return 
        ----------
        None 
        """
        
        self.height = height
        
    def getWidth(self):
        """
        The method get the width value 
        
        Parameters
        ----------
        None
        
        Return 
        ----------
        width : int 
            the integer  values of the rectangle width  
        """
        
        return self.width
        
    def getHeight(self):
        """
        The method get the height value 
        
        Parameters
        ----------
        None
        
        Return 
        ----------
        height : int 
            the integer  values of the rectangle height  
        """        
        return self.height 
    
    def area(self):
        """
        The method calculate the rectanle area  
        
        Parameters
        ----------
        None
        
        Return 
        ----------
        area : int 
            the integer  values of the rectangle area  
        """       
        
        return self.width * self.height
        
    def perimeter(self):
        """
        The method calculate the rectanle perimeter  
        
        Parameters
        ----------
        None
        
        Return 
        ----------
        perimeter : int 
            the integer  values of the rectangle perimeter  
        """ 
        
        return 2*(self.width + self.height)
    
    def __str__(self):
        """
        The method print the object state   
        
        Parameters
        ----------
        None
        
        Return 
        ----------
        string : str 
            String that shows object state such as its width and height  
        """
        
        return ("Width: " + str(self.width) + "\nHeight: " + str(self.height))
