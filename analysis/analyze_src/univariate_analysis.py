from abc import ABC, abstractmethod

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Abstract Base Class for Univariate Analysis Strategy
# -----------------------------------------------------
# This class defines a common interface for univariate analysis strategies.
# Subclasses must implement the analyze method.
class UnivariateAnalysisStrategy(ABC):
  @abstractmethod
  def analyze(self, df:pd.DataFrame, feature:str):
    """
    Perform univariate analysis on the specified feature of the dataframe.

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
class NumericalUnivariateAnalysis(UnivariateAnalysisStrategy):
  def analyze(self, df:pd.DataFrame, feature:str):
    """
    Perform univariate analysis on the specified numerical feature of the dataframe.

    Parameters:
    df (pd.DataFrame): The dataframe to analyze.
    feature (str): The numerical feature to analyze.

    Returns:
    None: This method visualizes the distribution of the numerical feature.
    """
    plt.figure(figsize=(10, 6))
    sns.histplot(df[feature], kde=True, bins=30)
    plt.title(f"Distribution of {feature}")
    plt.xlabel(feature)
    plt.ylabel("Frequency")
    plt.show()


# Concrete Class for categorical feature analysis Strategy
# ---------------------------------------------------------
# This class plots frequency distribution for categorical features.
class CategoricalUnivariateAnalysis(UnivariateAnalysisStrategy):
  def analyze(self, df:pd.DataFrame, feature:str):
    """
    Perform univariate analysis on the specified categorical feature of the dataframe.

    Parameters:
    df (pd.DataFrame): The dataframe to analyze.
    feature (str): The categorical feature to analyze.

    Returns:
    None: This method visualizes the frequency distribution of the categorical feature.
    """
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df, x=feature)
    plt.title(f"Frequency Distribution of {feature}")
    plt.xlabel(feature)
    plt.ylabel("Frequency")
    plt.xticks(rotation=45)
    plt.show()


# Context class for the univariate analysis strategy:
# ---------------------------------------------------
# This class is the context class for the univariate analysis strategy.
# It delegates the univariate analysis to the specified strategy.
class UnivariateAnalyzer:
  def __init__(self, strategy:UnivariateAnalysisStrategy):
    '''
      Initializes the univariate analyzer with the provided strategy.

      Parameters:
      strategy (UnivariateAnalysisStrategy): The strategy to be used for univariate analysis

      Returns:
      None
    '''
    self._strategy = strategy

  def analyze(self, df:pd.DataFrame, feature:str):
    """
      Perform univariate analysis on the specified feature of the dataframe.

      Parameters:
      df (pd.DataFrame): The dataframe to analyze.
      feature (str): The feature to analyze.

      Returns:
      None: This method visualizes the distribution of the feature.
    """
    self._strategy.analyze(df, feature)

  def set_strategy(self, strategy: UnivariateAnalysisStrategy):
    """
      Sets a new univariate analyzer with the provided strategy.

      Parameters:
      strategy (UnivariateAnalysisStrategy): The strategy to be used for univariate analysis

      Returns:
      None
    """
    self._strategy = strategy


# Example usage
if __name__ == "__main__":
    # Example usage of the UnivariateAnalyzer with different strategies.

    # Load the data
    # df = pd.read_csv('../extracted-data/your_data_file.csv')

    # Analyzing a numerical feature
    # analyzer = UnivariateAnalyzer(NumericalUnivariateAnalysis())
    # analyzer.execute_analysis(df, 'SalePrice')

    # Analyzing a categorical feature
    # analyzer.set_strategy(CategoricalUnivariateAnalysis())
    # analyzer.execute_analysis(df, 'Neighborhood')
    pass
