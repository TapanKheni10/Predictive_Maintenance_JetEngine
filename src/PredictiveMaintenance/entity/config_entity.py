from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

@dataclass
class DataValidationConfig:
    root_dir: Path
    unzip_file_dir: Path
    STATUS_FILE: str
    all_schema: dict

@dataclass
class DataTransformationConfig:
    root_dir: Path
    train_data_path: Path
    test_data_path: Path
    all_schema: list
    cols_to_drop: list

@dataclass
class ModelTrainerConfig:
    root_dir: Path
    x_train_data_path: Path
    y_train_data_path: Path
    model_name: str

@dataclass
class ModelEvaluationConfig:
    root_dir: Path
    x_test_data_path: Path
    truth_value_path: Path
    model_path: Path
    metric_name: str