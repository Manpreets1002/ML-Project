import sys

def error_msg_detail(error,error_detail:sys):
    _,_,error_tb = error_detail.exc_info()
    error_message = "Error occured in python script name [{0}] at line no. [{1}] with error message: [{2}]".format(
        error_tb.tb_frame.f_code.co_filename,
        error_tb.tb_lineno,
        error_detail
    )

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_msg_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message