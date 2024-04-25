from PredictiveMaintenance.entity import config_entity
from PredictiveMaintenance.utils.common import save_json
from pathlib import Path
import pandas as pd
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error,r2_score
import joblib


class ModelEvaluation:
    def __init__(self, config: config_entity.ModelEvaluationConfig_2):
        self.config = config

    def eval_metrics(self,actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        return rmse, mae, r2
    
    def save_results(self):

        test_x = pd.read_csv(self.config.X_test_path)
        test_y=pd.read_csv(self.config.ground_truth_data_path)
        model = joblib.load(self.config.model_path)

        print(test_x.shape)
        print(test_y.shape)
        
        predicted_qualities = model.predict(test_x)

        (rmse, mae, r2) = self.eval_metrics(test_y, predicted_qualities)
        
        # Saving metrics as local
        scores = {"rmse": rmse, "mae": mae, "r2": r2}
        save_json(path=Path(self.config.metric_file_name), data=scores)