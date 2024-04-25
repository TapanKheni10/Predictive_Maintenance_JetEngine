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
    
    def get_data_transformation_config(self) -> config_entity.DataTransformationConfig:
        config = self.config.data_transformation
        schema = self.schema.COLUMNS
        drop_schema = self.schema.COLS_TO_DROP_CATBOOST

        create_directories([config.root_dir])

        data_transformation_config = config_entity.DataTransformationConfig(
            root_dir=config.root_dir,
            train_data_path=config.train_data_path,
            test_data_path=config.test_data_path,
            all_schema=list(schema.keys()),
            cols_to_drop=list(drop_schema.keys())
        )

        return data_transformation_config
    
    def get_model_trainer_config(self) -> config_entity.ModelTrainerConfig:
        config = self.config.model_trainer
        params = self.params.CatBoostRegressor

        create_directories([config.root_dir])

        model_trainer_config = config_entity.ModelTrainerConfig(
            root_dir=config.root_dir,
            x_train_data_path=config.x_train_data_path,
            y_train_data_path=config.y_train_data_path,
            model_name=config.model_name,
            params=params
        )

        return model_trainer_config
    
    def get_model_evaluation_config(self) -> config_entity.ModelEvaluationConfig:
        config = self.config.model_evaluation
        params = self.params.CatBoostRegressor

        create_directories([config.root_dir])

        model_evaluation_config = config_entity.ModelEvaluationConfig(
            root_dir=config.root_dir,
            x_test_data_path=config.x_test_data_path,
            truth_value_path=config.truth_value_path,
            model_path=config.model_path,
            metric_name=config.metric_name
        )

        return model_evaluation_config
    
    def get_data_validation_config_2(self) -> config_entity.DataValidationConfig_2:
        config = self.config.data_validation_2
        schema = self.schema.COLUMNS

        create_directories([config.root_dir])

        data_validation_config = config_entity.DataValidationConfig_2(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            unzip_data_dir = config.unzip_data_dir,
            all_schema=schema,
        )

        return data_validation_config
    
    def get_data_transformation_config_2(self) -> config_entity.DataTransformationConfig_2:
        config = self.config.data_transformation_2
        cols_schema=self.schema.COLUMNS
        cols_to_drop_schema=self.schema.COLUMNS_TO_DROP_2

        create_directories([config.root_dir])

        data_transformation_config = config_entity.DataTransformationConfig_2(
            root_dir=config.root_dir,
            train_data_path=config.train_data_path,
            test_data_path=config.test_data_path,
            ground_truth_data_path=config.ground_truth_data_path,
            columns=list(cols_schema.keys()),
            columns_to_drop=list(cols_to_drop_schema.keys())
        )
        return data_transformation_config
    
    def get_model_trainer_config_2(self) -> config_entity.ModelTrainerConfig_2:
        config = self.config.model_trainer_2
        params = self.params.RandomForestRegressor_2

        create_directories([config.root_dir])

        model_trainer_config = config_entity.ModelTrainerConfig_2(
            root_dir=config.root_dir,
            X_train_path = config.X_train_path,
            y_train_path = config.y_train_path,
            X_test_path=config.X_test_path,
            ground_truth_data_apth=config.ground_truth_data_path,
            model_name = config.model_name,
            criterion=params.criterion,
            max_features=params.max_features,
            n_estimators=params.n_estimators,
            oob_score=params.oob_score
            
        )

        return model_trainer_config
    
    def get_model_evaluation_config_2(self) -> config_entity.ModelEvaluationConfig_2:
        config = self.config.model_evaluation_2
        params = self.params.RandomForestRegressor_2

        create_directories([config.root_dir])

        model_evaluation_config = config_entity.ModelEvaluationConfig_2(
            root_dir=config.root_dir,
            X_test_path=config.X_test_path,
            ground_truth_data_path=config.ground_truth_data_path,
            model_path = config.model_path,
            all_params=params,
            metric_file_name = config.metric_file_name,
           
        )

        return model_evaluation_config