import sys

def error_message_details(error, error_details):
    _, _, exc_tb = sys.exc_info()  # Corrected to use sys.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename  # Corrected method and attribute names
    error_message = "Error occurred in python script name[{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error))  # Corrected format usage
    return error_message  # Assuming you want to return or print the error message

class CustomException(Exception):
    def __init__(self, error, error_detail):
        error_message = error_message_details(error, error_detail)  # Generate the error message
        super().__init__(error_message)  # Corrected to call super() correctly
        self.error = error_message
        
 