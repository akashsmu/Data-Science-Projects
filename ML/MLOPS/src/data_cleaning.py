import logging
from abc import ABC, abstractmethod
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from typing import Union


class DataStrategy(ABC):
    @abstractmethod
    def handle_data(self,data:pd.DataFrame) -> Union[pd.DataFrame,pd.Series]:
        pass
# order_id,
# customer_id,
# order_status,
# order_purchase_timestamp,
# order_approved_at,
# order_delivered_carrier_date,
# order_delivered_customer_date,
# order_estimated_delivery_date,
# payment_sequential,
# payment_type,
# payment_installments,
# payment_value,
# customer_unique_id,
# customer_zip_code_prefix,
# customer_city,
# customer_state,
# order_item_id,
# product_id,
# seller_id,
# shipping_limit_date,
# price,freight_value,
# product_category_name,product_name_lenght,product_description_lenght,
# product_photos_qty,product_weight_g,product_length_cm,product_height_cm,
# product_width_cm,product_category_name_english,review_score,
# review_comment_message
class DataPreprocessingStrategy(DataStrategy):
    def handle_data(self, data: pd.DataFrame) -> pd.DataFrame:
        try:
            data = data.drop([
                "order_approved_at",
                "order_delivered_carrier_date",
                "order_delivered_customer_date",
                "order_estimated_delivery_date",
                "order_purchase_timestamp"
            ],axis =1 )
            data["product_weight_g"].fillna(data["product_weight_g"].median(),inplace=True)
            data["product_length_cm"].fillna(data["product_length_cm"].median(),inplace=True)
            data["product_height_cm"].fillna(data["product_height_cm"].median(),inplace=True)
            data["product_width_cm"].fillna(data["product_width_cm"].median(),inplace=True)
            data["review_comment_message"].fillna("No review",inplace=True)

            data = data.select_dtypes(include=[np.number])
            cols_to_drop = ['customer_zip_code_prefix',"order_item_id"]
            data = data.drop(cols_to_drop,axis=1)
            return data
        except Exception as e:
            logging.error("Error in preprocessing data {}".format(e))
            raise e
            
class DataDivideStrategy(DataStrategy):
    def handle_data(self, data: pd.DataFrame) -> Union[pd.DataFrame,pd.Series]:
        try:
            X = data.drop(["review_score"],axis = 1)
            y = data["review_score"]
            X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)
            return X_train,X_test,y_train,y_test
        except Exception as e:
            logging.error("Error id dividing data: {}".format(e))
            raise e

class DataCleaning:
    def __init__(self,data:pd.DataFrame,strategy:DataStrategy):
        self.data = data      
        self.strategy = strategy
    def handle_data(self) -> Union[pd.DataFrame,pd.Series]:
        try:
            return self.strategy.handle_data(self.data)
        except Exception as e:
            logging.error("Error in handling data : {}".format(e))
            raise e


