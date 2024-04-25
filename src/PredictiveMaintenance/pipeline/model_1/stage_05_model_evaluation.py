from PredictiveMaintenance.config.configuration import ConfigurationManager
from PredictiveMaintenance.components.model_1.model_evaluation import ModelEvaluation

class ModelEvaluationTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            model_evaluation_config = config.get_model_evaluation_config()
            obj = ModelEvaluation(model_evaluation_config)
            obj.save_matrix()
        except Exception as e:
            raise e
        
if __name__ == '__main__':
    pass