import logging, os
from time import strftime, gmtime

class St_logging:
    def __init__(self):
        self.file_handler=None

    def create_log(self):
        try:
            # Logging started for user
            # Creating a logging object
            logger_main = logging.getLogger(__name__)
            logger_main.setLevel(logging.DEBUG)
            # Creating logging message format  
            formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(message)s',"%Y-%m-%d %H:%M:%S")
            # Log File Path
            log_filepath = os.path.join(os.getcwd(),'Streamlit_Log')
            os.makedirs(log_filepath,exist_ok=True)
            log_filename = os.path.join(log_filepath+'/st_log_file'+strftime('%Y-%m-%d %H.%M.%S',gmtime())+'_.log')
            # Creating file handler which logs messages  
            self.file_handler = logging.FileHandler(log_filename)
            self.file_handler.setFormatter(formatter)
            logger_main.addHandler(self.file_handler)
            print(' * Logging started')
            return logger_main
        except Exception as e:
            print('Error occured due to '+ str(e))
            raise
    
    def exit_log(self, logger):
        logger.removeHandler(self.file_handler)
        logging.shutdown()
