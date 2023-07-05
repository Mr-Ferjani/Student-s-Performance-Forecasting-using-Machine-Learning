# Here we read the dataset, split it into trainm test and validation.
# to use custom exception we import os and sys
import os 
import sys
from src.exceptions import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
#used for defining variables
from dataclasses import dataclass 

#Testing data transform in the __main__ function
from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig
from src.components.model_trainer import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer


#from src.components.model_trainer import ModelTrainerConfig
#from src.components.model_trainer import ModelTrainer

# Input for the data ingestion would be [save location for raw ,training, testing, validation data]
# These inputs are configured in the dataclass 

@dataclass
class DataIngestionConfig:
    #Defining class variables
    train_data_path: str = os.path.join('artifacts','train.csv')
    test_data_path: str = os.path.join('artifacts','test.csv')
    raw_data_path: str = os.path.join('artifacts','raw.csv') 

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion module")
        try:
            df = pd.read_csv('notebook\data\stud.csv')
            logging.info('Read the dataset as a dataframe')

            #Creating directory artifacts
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            
            #Storing raw data to its folder
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header= True)

            logging.info("Train Test Split initiated")
            train_set, test_set =  train_test_split(df, test_size=0.2, random_state=2023)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header= True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header= True)
            logging.info("Data Ingestion is completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
                self.ingestion_config.raw_data_path
            )
        except Exception as e:
            raise CustomException(e,sys)


if __name__ == "__main__":
   obj = DataIngestion()
   train_data,test_data, raw_data = obj.initiate_data_ingestion()

   data_transformation=DataTransformation()
   tr_array, ts_array, _ = data_transformation.initiate_data_transformation(train_data,test_data)

   model_trainer = ModelTrainer()
   print(model_trainer.initiate_model_trainer(tr_array, ts_array))
