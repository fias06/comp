
DATE_SEPARATOR = "/"
DAY_LENGTH = 2
MONTH_LENGTH = 2
YEAR_LENGTH = 4
DATE_FORMAT_LENGTH = 10  #length of "DD/MM/YYYY" format
DATE_SEPARATOR_COUNT = 2  #no.of separators in "DD/MM/YYYY" 
DATE_SEPARATOR_POSITIONS = (2, 5)  #position separators in DD/MM/YYYY


def convert_date(date_str):
    """
    Checks if the input date string is in the correct format \
    "DD/MM/YYYY" and converts it into a dictionary with 'Day', \
    'Month', and 'Year' keys.

    Parameters:
    date_str (str): A string representing the date in \
    "DD/MM/YYYY" format.

    Returns:
    dict: A dictionary with keys 'Day', 'Month', and 'Year'\
    if input is valid.

    Raises:
    ValueError: If the input string is not in the correct format.

    Examples:
    >>> convert_date("02/05/2023")
    {'Day': '02', 'Month': '05', 'Year': '2023'}
    >>> convert_date("02/05/20/23")
    ValueError: Input format incorrect!
    >>> convert_date("1/10/24")
    ValueError: Input format incorrect!
    """
    
    date_list = date_str.split(DATE_SEPARATOR)
    length = [len(s) for s in date_list]
    

    if (len(date_str) == DATE_FORMAT_LENGTH and
        date_str.count(DATE_SEPARATOR) == DATE_SEPARATOR_COUNT and
        date_str[DATE_SEPARATOR_POSITIONS[0]] == DATE_SEPARATOR and
        date_str[DATE_SEPARATOR_POSITIONS[1]] == DATE_SEPARATOR and
        len(date_list) == 3 and
        len(date_list[0]) == DAY_LENGTH and
        len(date_list[1]) == MONTH_LENGTH and
        len(date_list[2]) == YEAR_LENGTH):
        return {"Day": date_list[0], "Month": date_list[1], "Year": date_list[2]}
    raise ValueError("Input format incorrect!")


        

def get_data(file_path):
    """ 
    Opens a file and reads its contents, make sure each character\
    in the file is either 0 or 1. Converts the file content\
    into a 2D list

    Parameters:
    file_path (str): Path to the file to be read.

    Returns:
    list: A 2D list containing integers (0 or 1) representing the\
    file's binary content.

    Raises:
    ValueError: If the file contains characters other than '0' or '1'.

    Examples:
    >>> get_data("small_data_error.txt")
    ValueError: File should contain only 0s and 1s!
    >>> get_data("small_data.txt")
    [[0, 1], [1, 0]]
    >>> get_data("new_file.txt")
    [[1, 1, 0], [0, 1, 0], [0, 0, 0], [1, 1, 0]]

    """
    
    data = []
    
    file =  open(file_path, 'r')
    for line in file:
        row = []
        i = 0
        while i < len(line) and line[i] != '\n':
            char = line[i]
            if char == '0':
                row.append(0)
            elif char == '1':
                row.append(1)
            else:
                raise ValueError("File should contain only 0s and 1s!")
            i += 1
        
        if row:  
            data.append(row)
    
    return data

print(get_data("Assignment 4/qrcode_binary.txt"))
