import logging
from abc import ABC, abstractmethod
import pandas as pd

# Logging setup
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(messages)s")


class MissingValueHandlingStrategy(ABC):
    @abstractmethod
    def handle(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Abstract method to handle missing values in the DataFrame

        :param df: Input data frame.
        :return: Missing values handled DataFrame.
        """
        pass


class DropMissingValuesStrategy(MissingValueHandlingStrategy):
    def __init__(self, axis=0, thresh=None):
        """
        Parameters:
        axis (int): 0 to drop rows with missing values, 1 to drop columns with missing values.
        thresh (int): The threshold for non-NA values. Rows/Columns with less than thresh non-NA values are dropped.
        """
        self.axis = axis
        self.thresh = thresh

    def handle(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Drops rows or columns with missing values based on the axis and threshold.
        :param df: Input data frame.
        :return: Missing values handled DataFrame.
        """
        logging.info(f"Dropping missing values with axis={self.axis} and thresh={self.thresh}")
        df_cleaned = df.dropna(axis=self.axis, thresh=self.thresh)
        logging.info(f"Missing values dropped.")
        return df_cleaned


class FillMissingValuesStrategy(MissingValueHandlingStrategy):
    ALLOWED_METHODS = {'mean', 'median', 'mode', 'constant'}

    def __init__(self, method="mean", fill_value=None):
        """
        :param method(str): Method to fill missing values ('mean', 'median', 'mode', or 'constant')
        :param fill_value(any):
        """
        if method not in self.ALLOWED_METHODS:
            logging.error(
                f"Invalid method '{method}'. Allowed methods are: {', '.join(self.ALLOWED_METHODS)}. Defaulting to "
                f"the method 'mean'.")
        self.method = method
        self.fill_value = fill_value

    def handle(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        :param df: The input DataFrame containing missing values.
        :return: The DataFrame with missing values filled.
        """
        logging.info(f"Filling missing values using method: {self.method}")
        df_cleaned = df.copy()

        if self.method == "mean":
            numeric_columns = df_cleaned.select_dtypes(include='number').columns
            df_cleaned[numeric_columns] = df_cleaned[numeric_columns].fillna(df_cleaned[numeric_columns].mean())

        elif self.method == "median":
            numeric_columns = df_cleaned.select_dtypes(include='number').columns
            df_cleaned[numeric_columns] = df_cleaned[numeric_columns].fillna(df_cleaned[numeric_columns].median())

        elif self.method == "mode":
            numeric_columns = df_cleaned.select_dtypes(include='number').columns
            df_cleaned[numeric_columns] = df_cleaned[numeric_columns].fillna(df_cleaned[numeric_columns].mode())

        elif self.method == "constant":
            df_cleaned = df_cleaned.fillna(self.fill_value)

        logging.info("Missing values filled.")
        return df_cleaned


# Context Class for Handling Missing Values Strategy
class MissingValueHandler:
    def __init__(self, strategy: MissingValueHandlingStrategy):
        """
        Initializes the MissingValueHandler with a specific missing value handling strategy.

        Parameters:
        strategy (MissingValueHandlingStrategy): The strategy to be used for handling missing values.
        """
        self._strategy = strategy

    def set_strategy(self, strategy: MissingValueHandlingStrategy):
        """
        Sets a new strategy for the MissingValueHandler.

        Parameters:
        strategy (MissingValueHandlingStrategy): The new strategy to be used for handling missing values.
        """
        logging.info(f"Switching missing value handling strategy.")
        self._strategy = strategy

    def handle_missing_values(self, df: pd.DataFrame):
        """
        Executes the missing value handling using the current strategy.

        Parameters:
        df (pd.DataFrame): The input DataFrame containing missing values.

        Returns:
        pd.DataFrame: The DataFrame with missing values handled.
        """
        logging.info("Executing missing value handling strategy.")
        return self._strategy.handle(df)


# Example usage
if __name__ == "__main__":
    # Example dataframe
    # df = pd.read_csv('../extracted-data/your_data_file.csv')

    # Initialize missing value handler with a specific strategy
    # missing_value_handler = MissingValueHandler(DropMissingValuesStrategy(axis=0, thresh=3))
    # df_cleaned = missing_value_handler.handle_missing_values(df)

    # Switch to filling missing values with mean
    # missing_value_handler.set_strategy(FillMissingValuesStrategy(method='mean'))
    # df_filled = missing_value_handler.handle_missing_values(df)

    pass
