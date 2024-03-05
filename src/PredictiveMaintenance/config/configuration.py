from PredictiveMaintenance.constants import CONFIG_YAML_FILE_PATH, SCHEMA_YAML_FILE_PATH, PARAMS_YAML_FILE_PATH
from PredictiveMaintenance.utils.common import read_yaml, create_directories
from PredictiveMaintenance.entity import config_entity

class ConfigurationManager:
    def __init__(self, 
                 config_filepath=CONFIG_YAML_FILE_PATH,
                 params_filepath=PARAMS_YAML_FILE_PATH, 
                 schema_filepath=SCHEMA_YAML_FILE_PATH):
        
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> config_entity.DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = config_entity.DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config
    
    def get_data_validation_config(self) -> config_entity.DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.COLUMNS

        create_directories([config.root_dir])

        data_validation_config = config_entity.DataValidationConfig(
            root_dir=config.root_dir,
            unzip_file_dir=config.unzip_file_dir,
            STATUS_FILE=config.STATUS_FILE,
            all_schema=schema
        )
        return data_validation_config