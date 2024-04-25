from PredictiveMaintenance.config.configuration import ConfigurationManager
from PredictiveMaintenance.components.model_2.data_validation import DataValiadtion
from src.PredictiveMaintenance import logger


STAGE_NAME = "Data Validation stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config_2()
        data_validation = DataValiadtion(config=data_validation_config)
        data_validation.validate_all_columns()

if __name__ == "__main__":
    pass