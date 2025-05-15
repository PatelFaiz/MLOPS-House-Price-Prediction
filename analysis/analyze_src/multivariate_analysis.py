from abc import ABC, abstractmethod

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Abstract Base Class for Multivariate Analysis
# ----------------------------------------------
# This class defines a template for performing multivariate analysis.
# Subclasses can override specific steps like correlation heatmap and pair plot generation.
class MultivariateAnalysisTemplate(ABC):
    def analyze(self, df: pd.DataFrame):
        """
        Perform multivariate analysis by creating correlation heatmap and pair plot on the provided dataframe.

        Parameters:
        df (pd.DataFrame): The dataframe to analyze.

        Returns:
        None: This method visualizes the multivariate analysis results.
        """
        self.generate_correlation_heatmap(df)
        self.generate_pairplot(df)

    
    @abstractmethod
    def generate_correlation_heatmap(self, df:pd.DataFrame):
        """
        Generate a correlation heatmap for the dataframe.

        Parameters:
        df (pd.DataFrame): The dataframe to analyze.

        Returns:
        None: This method visualizes the correlation heatmap.
        """
        pass

    @abstractmethod
    def generate_pairplot(self, df:pd.DataFrame):
        """
        Generate a pair plot for the dataframe.

        Parameters:
        df (pd.DataFrame): The dataframe to analyze.

        Returns:
        None: This method visualizes the pair plot.
        """
        pass

# Concrete class for multivariate analysis
class SimpleMultivariateAnalysis(MultivariateAnalysisTemplate):
    def generate_correlation_heatmap(self, df: pd.DataFrame):
        """
        Generate a correlation heatmap for the dataframe.

        Parameters:
        df (pd.DataFrame): The dataframe to analyze.

        Returns:
        None: This method visualizes the correlation heatmap.
        """
        plt.figure(figsize = (12,10))
        sns.heatmap(df.corr(), annot = True, fmt=".2f", cmap="coolwarm", linewidths=0.5)
        plt.title("Correlation Heatmap")
        plt.show()


    def generate_pairplot(self, df: pd.DataFrame):
        """
        Generate a pair plot for the dataframe.

        Parameters:
        df (pd.DataFrame): The dataframe to analyze.

        Returns:
        None: This method visualizes the pair plot.
        """
        sns.pairplot(df)
        plt.suptitle("Pair Plot of Selected Features", y=1.02)
        plt.show()