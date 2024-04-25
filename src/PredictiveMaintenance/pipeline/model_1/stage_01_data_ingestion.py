from PredictiveMaintenance.components.model_1.data_ingestion import DataIngestion
from PredictiveMaintenance.config import configuration

class DataIngestionTrainingPipeline:
    def __init__(self) -> None:
        pass
        
    def main(self):
        config = configuration.ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()

if __name__ == '__main__':
    pass