from zenml import pipeline, step, Model
from steps.data_ingestion_step import data_ingestion_step
from steps.handle_missing_values_step import handle_missing_values_step


@pipeline(
    model=Model(name='prices_predictor'),
)
def ml_pipeline():
    """ Defining machine learning pipeline """

    # Data ingestion step
    raw_data = data_ingestion_step(
        file_path="C:\\Learn\\House Price Prediction MLOPS Project\\data\\archive.zip"
    )

    filled_data = handle_missing_values_step(raw_data)
