from gc import enable
from zenml import pipeline
from steps.ingest_data import ingest_data
from steps.clean_data import clean_data
from steps.model_train import train_model
from steps.evaluation import evaluation_model

@pipeline(enable_cache=True)
def train_pipeline(data_path:str):
    df = ingest_data(data_path)
    clean_data(df)
    train_model(df)
    evaluation_model(df)

