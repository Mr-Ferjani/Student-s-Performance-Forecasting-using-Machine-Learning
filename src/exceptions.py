import sys
import src.logger as logger

def error_message_detail(error,error_detail:sys):
    #extract the file, line number of where the exception occured
    _, _, exec_tb  = error_detail.exc_info()
    file_name = exec_tb.tb_frame.f_code.co_filename
    error_message = f"Error occured in python script name [{file_name}], line number [{exec_tb.tb_lineno}], error message [{str(error)}]"

    return error_message

class CustomException(Exception): #Inhereting the python-builtin exception
    # Defining Constructor
    def __init__(self, error_message, error_details:sys):
        #inherit init function
        super().__init__(error_message)
        #Class Attribute
        self.error_message = error_message_detail(error_message,error_details)
        
    def __str__(self):
        return  self.error_message
    
if __name__ == "__main__":
    try:
        a = 1/0
    #Catching exception
    except Exception as e:
        logger.logging.info("Divided by zero error")
        #Contructor arguments must be passed (error_message, error details)
        raise CustomException(e,sys)
