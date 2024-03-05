import pandas as pd
import joblib
from PredictiveMaintenance import logger
from catboost import CatBoostRegressor
from PredictiveMaintenance.entity import config_entity
import os

class ModelTrainer:
    def __init__(self, config: config_entity.ModelTrainerConfig):
        self.config = config

    def train(self):
        X_train = pd.read_csv(self.config.x_train_data_path)
        y_train = pd.read_csv(self.config.y_train_data_path)

        catboost_regressor = CatBoostRegressor()
        catboost_regressor.fit(X_train, y_train)

        joblib.dump(catboost_regressor, os.path.join(self.config.root_dir, self.config.model_name))