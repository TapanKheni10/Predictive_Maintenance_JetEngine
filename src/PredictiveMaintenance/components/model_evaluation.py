import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from urllib.parse import urlparse
import numpy as np
import joblib
import os
from pathlib import Path
from PredictiveMaintenance import logger
from PredictiveMaintenance.entity import config_entity
from PredictiveMaintenance.utils.common import save_json

class ModelEvaluation:
    def __init__(self, config: config_entity.ModelEvaluationConfig):
        self.config = config

    def eval_matrix(self, y_true, y_pred):
        rmse = np.sqrt(mean_squared_error(y_pred=y_pred, y_true=y_true))
        mse = mean_squared_error(y_pred=y_pred, y_true=y_true)
        r2 = r2_score(y_pred=y_pred, y_true=y_true)
        return rmse, mse, r2
    
    def save_matrix(self):
        X_test = pd.read_csv(self.config.x_test_data_path)

        truth_value_path = self.config.truth_value_path

        dfs = {}
        for filename in os.listdir(truth_value_path):
            if filename.endswith(".txt"):
                file_path = os.path.join(truth_value_path, filename)

                df_name = os.path.splitext(filename)[0]

                df = pd.read_csv(file_path, sep="\s+", header=None, names=["RUL"])

                dfs[df_name] = df

                logger.info(f"DataFrame '{df_name}' has been created with shape: {df.shape}")
        
        RUL_FD001 = dfs["RUL_FD001"]

        y_test = RUL_FD001.iloc[:,-1]

        logger.info(f"y_test: {y_test.shape}")

        model = joblib.load(self.config.model_path)
        y_pred = model.predict(X_test)

        (rmse, mse, r2) = self.eval_matrix(y_true=y_test, y_pred=y_pred)

        scores = {"RMSE": rmse, "MSE": mse, "r2_score": r2}
        save_json(path=Path(os.path.join(self.config.root_dir, self.config.metric_name)), data=scores)