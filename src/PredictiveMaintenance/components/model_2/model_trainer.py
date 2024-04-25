import joblib
import os
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from PredictiveMaintenance.entity import config_entity




class ModelTrainer:
    def __init__(self, config: config_entity.ModelTrainerConfig_2):
        self.config = config


    
    def train(self):

        train_X = pd.read_csv(self.config.X_train_path)
        train_y = pd.read_csv(self.config.y_train_path)
        test_X = pd.read_csv(self.config.X_test_path)
        RUL=pd.read_csv(self.config.ground_truth_data_apth)
        

        lr = RandomForestRegressor(n_estimators=self.config.n_estimators, criterion=self.config.criterion, max_features=self.config.max_features, random_state=42)
        lr.fit(train_X, train_y)

        joblib.dump(lr, os.path.join(self.config.root_dir, self.config.model_name))