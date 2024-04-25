from PredictiveMaintenance.config.configuration import ConfigurationManager
from PredictiveMaintenance.components.model_2.model_evaluation import ModelEvaluation
from src.PredictiveMaintenance import logger


STAGE_NAME = "Model evaluation stage"


class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config_2()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.save_results()



if __name__ == '__main__':
    pass