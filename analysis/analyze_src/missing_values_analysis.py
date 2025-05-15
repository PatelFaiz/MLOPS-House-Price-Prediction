from abc import ABC, abstractmethod
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Abstract base template class for missing values analysis
class MissingValuesAnalysisTemplate(ABC):
  def analyze(self, df: pd.DataFrame):
    """
    Performs missing value analysis on the provided dataframe and prints the results.

    Parameters:
    df (pd.DataFrame): The dataframe to analyze.

    Returns:
    None: Analyze and prints the missing value analysis results.
    """
    self.identify_missing_values(df)
    self.plot_missing_values(df)
    # self.handle_missing_values(df)

  @abstractmethod
  def identify_missing_values(self, df: pd.DataFrame):
    """
    Identifies missing values in the dataframe.

    Parameters:
    df (pd.DataFrame): The dataframe to analyze.

    Returns:
    None: This methods prints count of missing values.
    """
    pass

  @abstractmethod
  def plot_missing_values(self, df: pd.DataFrame):
    """
    Plots the missing values in the dataframe.

    Parameters:
    df (pd.DataFrame): The dataframe to analyze.

    Returns:
    None: This method plots the missing value.
    """
    pass


# Concrete class for missing values analysis
class SimpleMissingValuesAnalysis(MissingValuesAnalysisTemplate):
  def identify_missing_values(self, df: pd.DataFrame):
    # Identify missing values in the dataframe
    res = pd.DataFrame()
    res['missing_values'] = df.isnull().sum()
    res = res[res['missing_values'] > 0]
    # print(f"\nMissing Values count by column:\n{missing_values}")

    res['missing_values_percentage'] = (res['missing_values'] / len(df)) * 100
    # print(f"\nMissing Values percentage by column:\n{missing_values_percentage}")
    print(f"\nMissing Values percentage by column:\n{res}")

  def plot_missing_values(self, df: pd.DataFrame):
    # Plot missing values in the dataframe
    print("Visualizing missing values...")
    plt.figure(figsize=(12, 8))
    sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
    plt.title("Missing values heatmap")
    plt.show()

  