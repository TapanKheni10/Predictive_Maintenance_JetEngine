from PredictiveMaintenance.config.configuration import ConfigurationManager
from PredictiveMaintenance.components.data_transformation import DataTransformation

class DataTransformationTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_transformation_config = config.get_data_transformation_config()
            obj = DataTransformation(config=data_transformation_config)
            obj.do_data_transformation()
        except Exception as e:
            raise e 
        
if __name__ == '__main__':
    pass