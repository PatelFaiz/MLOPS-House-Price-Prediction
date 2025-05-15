import os
import zipfile
from abc import ABC, abstractmethod
import logging
import pandas as pd


# Abstract class for data Ingestor (factory)
class DataIngestor(ABC):
    @abstractmethod
    def ingest(self, file_path: str) -> pd.DataFrame:
        pass


# Abstract class for data Ingestor (factory)
class ZipDataIngestor(DataIngestor):
    def ingest(self, file_path: str) -> pd.DataFrame:
        """ Extracts data from zip file and returns a pandas DataFrame """

        if not file_path.endswith('.zip'):
            raise ValueError("Provided file is not a .zip file.")

        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall("extracted_data")

        extracted_files = os.listdir("extracted_data")
        print("extracted_files: ", extracted_files)
        csv_files = [f for f in extracted_files if f.endswith('.csv')]
        if len(csv_files) == 0:
            raise FileNotFoundError("No csv files found in the zip file.")
        elif len(csv_files) > 1:
            raise ValueError("Multiple csv files found in the zip file please specify which one to use.")

        csv_file_path = os.path.join("extracted_data", csv_files[0])
        df = pd.read_csv(csv_file_path)
        return df


# Abstract class for factory
class DataIngestorFactory:
    @staticmethod
    def get_data_ingestor(file_extension: str) -> DataIngestor:
        """Returns the appropriate DataIngestor based on file extension."""
        if file_extension == ".zip" or file_extension == 'zip':
            return ZipDataIngestor()
        else:
            raise ValueError(f"No ingestor available for file extension: {file_extension}")


# Example usage
if __name__ == "__main__":
    # # Specify the file path
    # file_path = "C:\\Learn\\House Price Prediction MLOPS Project\\data\\archive.zip"

    # # Determine the file extension
    # file_extension = os.path.splitext(file_path)[1]

    # # Get the appropriate DataIngestor
    # data_ingestor = DataIngestorFactory.get_data_ingestor(file_extension)

    # # Ingest the data and load it into a DataFrame
    # df = data_ingestor.ingest(file_path)

    # # Now df contains the DataFrame from the extracted CSV
    # print(df.head())  # Display the first few rows of the DataFrame
    pass
