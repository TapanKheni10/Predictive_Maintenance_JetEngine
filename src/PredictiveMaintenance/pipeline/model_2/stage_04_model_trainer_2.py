from PredictiveMaintenance.config.configuration import ConfigurationManager
from PredictiveMaintenance.components.model_2.model_trainer import ModelTrainer
from src.PredictiveMaintenance import logger


STAGE_NAME = "Model Trainer stage"


class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config_2()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()



if __name__ == '__main__':
    pass