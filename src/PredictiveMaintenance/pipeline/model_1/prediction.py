import joblib
import numpy as np
import pandas as pd
from pathlib import Path
from PredictiveMaintenance import logger


class PredictionPipeline:
    def __init__(self):
        self.model = joblib.load(Path('artifacts/model_trainer/model.joblib'))

    def predict(self, data):
        prediction = int(self.model.predict(data))
        logger.info(f"Predicted RUL: {prediction}")
        return prediction