from abc import ABC, abstractmethod

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Abstract Base Class for Bivariate Analysis Strategy
# -----------------------------------------------------
# This class defines a common interface for Bivariate analysis strategies.
# Subclasses must implement the analyze method.
class BivariateAnalysisStrategy(ABC):
  @abstractmethod
  def analyze(self, df:pd.DataFrame, feature1:str, feature2:str):
    """
    Perform Bivariate analysis on the specified feature of the dataframe.

    Parameters:
    df (pd.DataFrame): The dataframe to analyze.
    feature (str): The feature to analyze.

    Returns:
    None: This method visualizes the distribution of the feature.
    """
    pass

# Concrete Class for numerical feature analysis Strategy
# ---------------------------------------------------------
# This class plots histogram for numerical features.
class NumericalVsNumericalAnalysis(BivariateAnalysisStrategy):
  def analyze(self, df:pd.DataFrame, feature1:str, feature2:str):
    """
      Plots the relationship between two numerical features using a scatter plot.

      Parameters:
      df (pd.DataFrame): The dataframe containing the data.
      feature1 (str): The name of the first numerical feature/column to be analyzed.
      feature2 (str): The name of the second numerical feature/column to be analyzed.

      Returns:
      None: Displays a scatter plot showing the relationship between the two features.
    """
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x=feature1, y=feature2)
    plt.title(f"Scatter Plot of {feature1} vs {feature2}")
    plt.xlabel(feature1)
    plt.ylabel(feature2)
    plt.show()


# Concrete Class for categorical feature analysis Strategy
# ---------------------------------------------------------
# This class plots frequency distribution for categorical features.
class CategoricalVsNumericalBivariateAnalysis(BivariateAnalysisStrategy):
  def analyze(self, df:pd.DataFrame, feature1:str, feature2:str):
    """
      Plots the relationship between a categorical feature and a numerical feature using a box plot.

      Parameters:
      df (pd.DataFrame): The dataframe containing the data.
      feature1 (str): The name of the categorical feature/column to be analyzed.
      feature2 (str): The name of the numerical feature/column to be analyzed.

      Returns:
      None: Displays a box plot showing the relationship between the categorical and numerical features.
    """
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, x=feature1, y=feature2)
    plt.title(f"Box Plot of {feature1} vs {feature2}")
    plt.xlabel(feature1)
    plt.ylabel(feature2)
    plt.xticks(rotation=45)
    plt.show()


# Context class for the Bivariate analysis strategy:
# ---------------------------------------------------
# This class is the context class for the Bivariate analysis strategy.
# It delegates the Bivariate analysis to the specified strategy.
class BivariateAnalyzer:
  def __init__(self, strategy:BivariateAnalysisStrategy):
    '''
      Initializes the Bivariate analyzer with the provided strategy.

      Parameters:
      strategy (BivariateAnalysisStrategy): The strategy to be used for Bivariate analysis

      Returns:
      None
    '''
    self._strategy = strategy

  def analyze(self, df:pd.DataFrame, feature1:str, feature2:str):
    """
      Perform Bivariate analysis on the specified feature of the dataframe.

      Parameters:
      df (pd.DataFrame): The dataframe to analyze.
      feature (str): The feature to analyze.

      Returns:
      None: This method visualizes the distribution of the feature.
    """
    self._strategy.analyze(df, feature1, feature2)

  def set_strategy(self, strategy: BivariateAnalysisStrategy):
    """
      Sets a new Bivariate analyzer with the provided strategy.

      Parameters:
      strategy (BivariateAnalysisStrategy): The strategy to be used for Bivariate analysis

      Returns:
      None
    """
    self._strategy = strategy


# Example usage
if __name__ == "__main__":
    # Example usage of the BivariateAnalyzer with different strategies.

    # Load the data
    # df = pd.read_csv('../extracted-data/your_data_file.csv')

    # Analyzing a numerical feature
    # analyzer = BivariateAnalyzer(NumericalBivariateAnalysis())
    # analyzer.execute_analysis(df, 'SalePrice')

    # Analyzing a categorical feature
    # analyzer.set_strategy(CategoricalBivariateAnalysis())
    # analyzer.execute_analysis(df, 'Neighborhood')
    pass
