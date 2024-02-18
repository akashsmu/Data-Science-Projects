import logging

from sklearn.base import RegressorMixin
from zenml import step
import pandas as pd
from src.evaluation import MSE,RMSE,R2
from typing import Tuple
from typing_extensions import Annotated
from zenml.client import Client
import mlflow
experiment_tracker = Client().active_stack.experiment_tracker




@step(experiment_tracker=experiment_tracker.name)
def evaluation_model(model:RegressorMixin,
                     X_test:pd.DataFrame,
                     y_test:pd.DataFrame,
                     ) -> Tuple[
                        Annotated[float,'mse'],
                        Annotated[float,"r2_score"],
                        Annotated[float,"rmse"],
                     ]:
    try:
        prediction = model.predict(X_test)
        mse_class = MSE()
        mse = mse_class.calculate_scores(y_test,prediction)
        mlflow.log_metric("mse",mse)
        r2_class = R2()
        r2 = r2_class.calculate_scores(y_test,prediction)
        mlflow.log_metric("r2",r2)
        rmse_class = RMSE()
        rmse = rmse_class.calculate_scores(y_test,prediction)
        mlflow.log_metric("rmse",rmse)
        return mse,r2,rmse
    except Exception as e:
        pass
