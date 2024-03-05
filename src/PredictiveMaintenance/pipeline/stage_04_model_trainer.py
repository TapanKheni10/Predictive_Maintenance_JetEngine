from PredictiveMaintenance.config.configuration import ConfigurationManager
from PredictiveMaintenance.components.model_trainer import ModelTrainer

class ModelTrainerTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            model_trainer_config = config.get_model_trainer_config()
            obj = ModelTrainer(config=model_trainer_config)
            obj.train()
        except Exception as e:
            raise e
        
if __name__ == '__main__':
    pass