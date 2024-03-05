from PredictiveMaintenance.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from PredictiveMaintenance.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from PredictiveMaintenance.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from PredictiveMaintenance.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from PredictiveMaintenance.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline
from PredictiveMaintenance import logger

STAGE_NAME = "data ingestion stage"

try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "data validation stage"

try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "data transformation stage"

try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
    obj = DataTransformationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "model trainer stage"

try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
    obj = ModelTrainerTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "model evaluation stage"

try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
    obj = ModelEvaluationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e