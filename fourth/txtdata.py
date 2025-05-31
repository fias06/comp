import copy
from helper import get_data

BLOCK_CHAR = "\u2588"  #unicode char for pretty_save()
SPACE_CHAR = " " #space character
PIXEL_WIDTH = 2  #number of char per pixel in pretty_save()

#error messages
INDEX_ERROR_MSG = "Index out of bound!"
DIMENSION_MISMATCH_MSG = "Data dimensions do not match!"


class TxtData:
    """
    A class for storing and handling 2D binary data (such as QR codes) 
    from a list or a text file.

    Attributes:

    last_update_date (dict): Dictionary containing date components 
    owner (str): Name of the QR code owner
    data (TxtData): TxtData object containing the binary QR code pattern
    error_correction (float): Allowed error tolerance ratio (0.0 to 1.0)

    """

    def __init__(self, data):
        """
        Initializes a TxtData object with a deep copy of the input data,
        and sets the number of rows and columns based on the data structure.

        Parameters:
        data (list of list of int): A 2D list representing binary data.

        Returns:
        None

        Examples:
        >>> mylist = [[1,3,4,5],[1,3,45]]
        >>> trial1 = TxtData(mylist)
        >>> trial1.cols
        4
        >>> mylist = [[1,3,4,5],[1,3,4,5]]
        >>> trial1 = TxtData(mylist)
        >>> trial1.rows
        2
        >>> my_list = get_data("qrcode_binary.txt")
        >>> trial1 = TxtData(my_list)
        >>> trial1.cols
        33

        """

        #self for each attribute
        self.data = copy.deepcopy(data)
        self.rows = len(data)
        self.cols = len(data[0])
    
    def __str__(self):
        """
        Returns a string summarizing the dimensions of the TxtData object.

        Parameters:
        None

        Returns:
        str: A message stating the number of rows and columns.

        Examples:
        >>> my_list = get_data("Assignment 4/A4_TextData/qrcode_binary.txt")
        >>> trial1 = TxtData(my_list)
        >>> print(trial1)
        This TxtData object has 34 rows and 33 columns.
        >>> mylist3 = [[1,3,4,5],[1,3,4,5]]
        >>> trial1 = TxtData(mylist3)
        >>> print(trial1)
        This TxtData object has 2 rows and 4 columns.
        >>> mylist2 = [[1,3,45]]
        >>> trial1 = TxtData(mylist)
        >>> print(trial1)
        This TxtData object has 1 rows and 3 columns.

        """
        #returns the required text
        return "This TxtData object has "+str(self.rows) + \
            " rows and " + str(self.cols) + " columns."
    
    def get_pixels(self):
        """
        Calculates and returns the total number of pixels (elements) in the data.

        Parameters:
        None

        Returns:
        int: Total number of elements (rows * columns).

        Examples:

        >>> mylist = [[1,3,4,5],[1,3,4,5]]
        >>> trial1 = TxtData(mylist)
        >>> trial1.get_pixels(mylist)
        8
        >>> mylist = [[1,3,4,5]]
        >>> trial1 = TxtData(mylist)
        >>> trial1.get_pixels(mylist)
        4
        >>> mylist = [[1,3,4],[2,4,5],[4,6,3]]
        >>> trial1 = TxtData(mylist)
        >>> trial1.get_pixels(mylist)
        9

        """

        #total pixels is rows x cols
        return self.rows * self.cols
    
    def get_data_at(self, row, col):
        """
        Retrieves the value at a specified row and column position in the data.

        Parameters:
        row (int): Row index.
        col (int): Column index.

        Returns:
        int: The value at the given position.

        Raises:
        ValueError: If the index is out of bounds.

        Examples:
        >>> mylist = [[1,3,4,5],[1,3,4,5]]
        >>> trial1 = TxtData(mylist)
        >>> print(trial1.get_data_at(1,1))
        3
        >>> mylist = [[1,3,4,5],[1,3,4,5]]
        >>> trial1 = TxtData(mylist)
        >>> print(trial1.get_data_at(0,0))
        1
        >>> mylist = [[1,3,4,5],[1,3,4,5]]
        >>> trial1 = TxtData(mylist)
        >>> print(trial1.get_data_at(1,1))
        ValueError: Index out of bounds!

        """
        #condition set for get_data_at()
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            raise ValueError(INDEX_ERROR_MSG)
        return self.data[row][col]

    def pretty_save(self, file_name):
        """
        Saves the data to a file as a visual representation, \
        where 1s are represented by two solid block characters\
        and 0s are represented by spaces.

        Parameters:
        file_name (str): Name of the file to write the output.

        Returns:
        None

        Examples:
        >>> data = get_data("Assignment 4/A4_TextData/small_data.txt")
       >>> txt = TxtData(data)
       >>> txt.pretty_save("new.txt")
           ██
        ██  
        
        >>> data = get_data("hi.txt")
        >>> txt = TxtData(data)
        >>> txt.pretty_save("new.txt")
        ██████  ██████         
        
        >>> data = get_data("hi2.txt")
        >>> txt = TxtData(data)
        >>> txt.pretty_save("new.txt")  
        ████

        """

        fi = open(file_name, 'w') #for opening a file in write
        for row in self.data: #goes through each element
            line = []
            for value in row:
                if value == 1:
                    #adds a block
                    line.append(BLOCK_CHAR * PIXEL_WIDTH)
                else:
                    #adds a space
                    line.append(SPACE_CHAR * PIXEL_WIDTH)
            fi.write(''.join(line) + '\n') 
        fi.close()

    def equals(self, another_data):
        """
        Compares this TxtData object to another for exact equality\
        in dimensions and values.

        Parameters:
        another_data (TxtData): Another TxtData object to compare.

        Returns:
        bool: True if the data and dimensions match exactly, False otherwise.

        Examples:
        >>> data1 = [[1,0,1],[0,1,0],[1,0,1]]
        >>> txt1 = TxtData(data1)
        >>> txt2 = TxtData(data1)
        >>> print(txt1.equals(txt2))  
        True
        >>> data1 = [[1,0,1],[0,1,0],[1,0,1]]
        >>> data2 = [[1,0,1],[0,2,0],[1,0,1]]
        >>> txt1 = TxtData(data1)
        >>> txt2 = TxtData(data2)
        >>> print(txt1.equals(txt2)) 
        False
        >>> data1 = [[1,0,1],[0,1,0],[1,0,1]]
        >>> data2 = [[1,0],[0,1],[1,0]]
        >>> txt1 = TxtData(data1)
        >>> txt2 = TxtData(data2)
        >>> print(txt1.equals(txt2))  
        False

        """
        if self.rows != another_data.rows or self.cols != another_data.cols:
            return False
        #nested loop for rows and cols of each element
        for r in range(self.rows):
            for c in range(self.cols):
                if self.data[r][c] != another_data.data[r][c]:
                    return False
        return True
    
    def approximately_equals(self, another_data, precision):
        """ 
        Checks whether this TxtData object is approximately \
        equal to another one, based on the fraction of differing\
        elements allowed (precision).

        Parameters:
        another_data (TxtData): Another TxtData object to compare.
        precision (float): The maximum allowable fraction of 
        differing elements.

        Returns:
        bool: True if the proportion of differing elements is \
        less than or equal to precision.

        Examples:
        >>> my_list_simple_1 = [[1,2,3],[4,5,6]]
        >>> my_list_simple_2 = [[1,2,3],[7,8,9]]
        >>> my_txt_simple_1 = TxtData(my_list_simple_1)
        >>> my_txt_simple_2 = TxtData(my_list_simple_2)
        >>> print(my_txt_simple_1.approximately_equals(my_txt_simple_2, 0.5))
        True 
        >>> data1 = [[1,0,1], [0,1,0], [1,0,1]]
        >>> data2 = [[1,0,1], [0,0,0], [1,0,1]] 
        >>> txt1 = TxtData(data1)
        >>> txt2 = TxtData(data2)
        >>> print(txt1.approximately_equals(txt2, 0.1))
        False
        >>> data1 = [[1,0,1], [0,1,0], [1,0,1]]
        >>> data2 = [[1,0,1], [0,0,0], [1,0,1]] 
        >>> txt1 = TxtData(data1)
        >>> txt2 = TxtData(data2)
        >>> print(txt1.approximately_equals(txt2, 0.5))
        True
        """
        #to check if its rows/cols are equal
        if self.rows != another_data.rows or\
         self.cols != another_data.cols:
            return False
        
        impr = 0
        
        #condiion for approx equal
        for r in range(self.rows):
            for c in range(self.cols):
                if self.data[r][c] != another_data.data[r][c]:
                    impr += 1
                    
        total_pix = self.rows*self.cols
        incon_rate = impr/total_pix
        
        return incon_rate <= precision
