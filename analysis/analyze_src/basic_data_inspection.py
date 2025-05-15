from abc import ABC, abstractmethod
import pandas as pd

# Abstract class for data inspection strategy
class DataInspectionStrategy(ABC):
    @abstractmethod
    def inspect(self, df: pd.DataFrame):
      """
        Perform a specific type of data inspection.

        Parameters:
        df (pd.DataFrame): The dataframe on which the inspection is to be performed.

        Returns:
        None: This method prints the inspection results directly.
        """
      pass

class DataTypeInspectionStrategy(DataInspectionStrategy):
  def inspect(self, df: pd.DataFrame):
    """
      Perform a data type inspection on the dataframe.

      Parameters:
        df (pd.DataFrame): The dataframe to be inspected.

      Returns:
      None: Prints the data types and non-null counts to the console.
    """
    print("\nData types and non-null counts:")
    print(df.info())

class SummaryStatisticInspectionStrategy(DataInspectionStrategy):
  def inspect(self, df: pd.DataFrame):
    """
      Summarize every column of the data frame.

      Parameters:
        df (pd.DataFrame): The dataframe to be inspected.

      Returns:
      None: Prints summary of numerical and Categorical Features.  
    """
    print("\nSummary statistics (Numerical Features):")
    print(df.describe())
    print("\nSummary statistics (Categorical Features):")
    print(df.describe(include=["O"]))

# Context class for the data inspection strategy:
class DataInspector:
  def __init__(self, strategy:DataInspectionStrategy):
    '''
      Initializes the data inspector with the provided strategy.

      Parameters:
      strategy (DataInspectionStrategy): The strategy to be used for data inspection

      Returns:
      None
    '''
    self._strategy = strategy

  def set_strategy(self, strategy: DataInspectionStrategy):
    """
      Sets a new data inspector with the provided strategy.

      Parameters:
      strategy (DataInspectionStrategy): The strategy to be used for data inspection

      Returns:
      None
    """
    self._strategy = strategy

  def execute_inspection(self, df:pd.DataFrame):
    """
      Executes the inspect function of the set strategy

      Parameters:
      df (DataFrame): The dataframe to be inspected.

      Returns:
      None
    """

    self._strategy.inspect(df)


if __name__ == "__main__":
    # Example usage of the DataInspector with different strategies.

    # Load the data
    # df = pd.read_csv('../extracted-data/your_data_file.csv')

    # Initialize the Data Inspector with a specific strategy
    # inspector = DataInspector(DataTypesInspectionStrategy())
    # inspector.execute_inspection(df)

    # Change strategy to Summary Statistics and execute
    # inspector.set_strategy(SummaryStatisticsInspectionStrategy())
    # inspector.execute_inspection(df)
    pass
