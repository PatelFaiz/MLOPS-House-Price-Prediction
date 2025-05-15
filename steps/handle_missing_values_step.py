import pandas as pd
from zenml import step
from src.handle_missing_values import MissingValueHandler, MissingValueHandlingStrategy, FillMissingValuesStrategy, \
    DropMissingValuesStrategy


@step
def handle_missing_values_step(data: pd.DataFrame, strategy: str = "mean") -> pd.DataFrame:
    """Handles missing values using MissingValueHandler and the specified strategy."""

    if strategy == "drop":
        handler = MissingValueHandler(DropMissingValuesStrategy(axis=0))
    elif strategy in ['mean', 'median', 'mode', 'constant']:
        handler = MissingValueHandler(FillMissingValuesStrategy(method=strategy))
    else:
        raise ValueError(f"Unsupported missing value handling strategy: {strategy}")

    cleaned_df = handler.handle_missing_values(data)
    return cleaned_df
