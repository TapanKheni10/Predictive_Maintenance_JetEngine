from PredictiveMaintenance.pipeline.model_1 import (
    stage_01_data_ingestion,
    stage_02_data_validation,
    stage_03_data_transformation,
    stage_04_model_trainer,
    stage_05_model_evaluation
)
from PredictiveMaintenance.pipeline.model_2 import (
    stage_02_data_validation_2,
    stage_03_data_transformation_2,
    stage_04_model_trainer_2,
    stage_05_model_evaluation_2
)
from PredictiveMaintenance import logger

STAGE_NAME = "data ingestion stage"

try:
    logger.info(f">>>>>>> stage {STAGE_NAME} (model_1) started <<<<<<<")
    obj = stage_01_data_ingestion.DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} (model_1) completed <<<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "data validation stage"

try:
    logger.info(f">>>>>>> stage {STAGE_NAME} (model_1) started <<<<<<<")
    obj = stage_02_data_validation.DataValidationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} (model_1) completed <<<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

try:
    logger.info(f">>>>>> stage {STAGE_NAME} (model_2) started <<<<<<")
    obj = stage_02_data_validation_2.DataValidationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} (model_2) completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "data transformation stage"

try:
    logger.info(f">>>>>>> stage {STAGE_NAME} (model_1) started <<<<<<<")
    obj = stage_03_data_transformation.DataTransformationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} (model_1) completed <<<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

try:
    logger.info(f">>>>>>> stage {STAGE_NAME} (model_2) started <<<<<<<")
    obj = stage_03_data_transformation_2.DataTransformationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} (model_2) completed <<<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "model trainer stage"

try:
    logger.info(f">>>>>>> stage {STAGE_NAME} (model_1) started <<<<<<<")
    obj = stage_04_model_trainer.ModelTrainerTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} (model_1) completed <<<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

try:
    logger.info(f">>>>>> stage {STAGE_NAME} (model_2) started <<<<<<")
    obj = stage_04_model_trainer_2.ModelTrainerTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} (model_2) completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "model evaluation stage"

try:
    logger.info(f">>>>>>> stage {STAGE_NAME} (model_1) started <<<<<<<")
    obj = stage_05_model_evaluation.ModelEvaluationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} (model_1) completed <<<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

try:
    logger.info(f">>>>>> stage {STAGE_NAME} (model_2) started <<<<<<")
    obj = stage_05_model_evaluation_2.ModelEvaluationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} (model_2) completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e