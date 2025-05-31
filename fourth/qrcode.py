from helper import convert_date, get_data
from txtdata import TxtData

DEFAULT_DATE = "00/00/0000"
DEFAULT_OWNER = "Default Owner"
DEFAULT_ERROR_CORRECTION = 0.0


class QRCode:
    """
    a class for a QR code with associated\
     metadata and binary data.

    Attributes:

    last_update_date (dict): a dictionary with 
    'Day', 'Month', 'Year' for the update date.
    owner (str): The name of the person who owns the QR code.
    TxtData (TxtData): A TxtData object the binary of the QR code.
    error_correction (float): A float value for allowed\
     mismatch tolerance in comparisons.
    """


    def __init__(self, file_path, last_update_date=DEFAULT_DATE,\
     owner=DEFAULT_OWNER, error_correction=DEFAULT_ERROR_CORRECTION):
        """
        sets a QRCode object from a given file and metadata.

        Parameters:
        file_path (str): The path to the text file containing \
        the QR code data.

        last_update_date (str): The date of the last update in \
        "DD/MM/YYYY" format (default: "00/00/0000").

        owner (str): The name of the QR code owner (default: "Default Owner").
        error_correction (float): Allowed proportion of \
        mismatched pixels for comparisons (default: 0.0).

        Returns:
        None

        Examples:
        >>> q1 = QRCode("Assignment 4/A4_TextData/qrcode_binary.txt", \
        "15/03/2024", "Alice", 0.1)
        >>> q1.owner
        'Alice'
        >>> q1.last_update_date['Year']
        '2024'
        """
        #self for all attributes
        self.last_update_date = convert_date(last_update_date)
        self.owner = owner
        self.data = TxtData(get_data(file_path))
        self.error_correction = error_correction

    def __str__(self):
        """
        returns a formatted string with metadata and data summary.

        Parameters:
        None

        Returns:
        str: a readable summary of the QRCode instance.

        Examples:
        >>> q1 = QRCode("qrcode_binary.txt",\"15/03/2024", "Alice", 0.1)
        >>> print(q1)
        The QR code was created by Alice and last updated in 2024.
        The details regarding the QR code file are as follows:
        This TxtData object has 34 rows and 33 columns.

        >>> q1 = QRCode("trial2.txt",\"05/03/2021", "Max", 0.1)
        >>> print(q1)
        The QR code was created by Max and last updated in 2021.
        The details regarding the QR code file are as follows:
        This TxtData object has 4 rows and 3 columns.

        >>> q1 = QRCode("Assignment 4/A4_TextData/qrcode_binary.txt",\
         "10/12/2013", "Saif", 0.1)
        >>> print(q1)
        The QR code was created by Saif and last updated in 2013.
        The details regarding the QR code file are as follows:
        This TxtData object has 6 rows and 23 columns.
    
        """

        #returns all the mentioned points
        return ("The QR code was created by "+str(self.owner)+\
        " and last updated in "+str(self.last_update_date['Year'])+".\n"\
                "The details regarding the QR code file are as follows:\n"\
                +str(self.data))

    def equals(self, another_qrcode):
        """
        checks if another QRCode object is exactly equal to this one,
        based on both binary data and error correction rate.

        Parameters:
        another_qrcode (QRCode): Another QRCode to compare.

        Returns:
        bool: True if the QR codes are same, False otherwise.

        Examples:
        >>> q1 = QRCode("file1.txt", "01/01/2024", "Owner1", 0.1)
        >>> q2 = QRCode("file1.txt", "01/01/2024", "Owner2", 0.1)
        >>> q1.equals(q2)
        True
        >>> q1 = QRCode("file1.txt", "01/01/2024", "Owner1", 0.1)
        >>> q2 = QRCode("trial2.txt", "01/01/2024", "Owner2", 0.1)
        >>> q1.equals(q2)
        False
        >>> q1 = QRCode("trail1.txt", "01/01/2024", "Owner1", 0.1)
        >>> q2 = QRCode("trial2.txt", "01/01/2024", "Owner2", 0.1)
        >>> q1.equals(q2)
        False
        """
        return (self.data.equals(another_qrcode.data) and \
        self.error_correction == another_qrcode.error_correction)
    def is_corrupted(self, precise_qrcode):
        """
        checks if this QRCode is corrupted compared to a 
        precise reference version, using the error correction 
        level to define acceptable differences.

        Parameters:
        precise_qrcode (QRCode): The accurate reference QRCode object.

        Returns:
        bool: True if this QR code differs more than allowed by 
        error_correction, False otherwise.

        Examples:
        >>> q1 = QRCode("corrupted.txt", "01/01/2024", "Owner", 0.1)
        >>> q2 = QRCode("precise.txt", "01/01/2024", "Owner", 0.1)
        >>> q1.is_corrupted(q2)
        True
        """

        return not self.data.approximately_equals(precise_qrcode.data,\
        self.error_correction)
