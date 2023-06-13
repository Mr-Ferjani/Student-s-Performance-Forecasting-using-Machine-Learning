#The purpose is to log all the execution information to properly track the code
# Whenever we get an exception, we log it in a logger file    
import logging
import os
from datetime import datetime

# Log file name
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(),"logs")
# Make directory and allow appending new log files insode dir
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

#Logger basic configuration
logging.basicConfig(
    filename = LOG_FILE_PATH,
    format = " [%(asctime)s] %(lineno)d - %(levelname)s - %(message)s ",
    level = logging.INFO,
)

if __name__ == "__main__":
    logging.info("Logging has started")