from PredictiveMaintenance.entity import config_entity
from src.PredictiveMaintenance import logger
import pandas as pd
import os
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer


class DataTransformation:
    def __init__(self, config: config_entity.DataTransformationConfig_2):
        logger.info("data transformation started")
        self.config = config 
    
    def Calculate_RUL(self,df):
        max_cycles = df.groupby('Engine Number')['Times/ in cycle'].max()
        merged = df.merge(max_cycles.to_frame(name='max_time_cycle'), left_on='Engine Number',right_index=True)
        merged["RUL"] = merged["max_time_cycle"] - merged['Times/ in cycle']
        merged["RUL"].head(3)
        merged = merged.drop("max_time_cycle", axis=1)
        return merged
    
    def impute_outliers(self,data):
        sensors=data.drop(columns=['Engine Number', 'Times/ in cycle'],axis=1)
        sensors=data.columns
        for col in sensors:
            q1 = data[col].quantile(0.25)
            q3 = data[col].quantile(0.75)
            iqr = q3 - q1
            lower_bound = q1 - (1.5 * iqr)
            upper_bound = q3 + (1.5 * iqr)

            data.loc[data[col] < lower_bound, col] = data[col].median()
            data.loc[data[col] > upper_bound, col] = data[col].median()
        return data
    
    def train_test_spliting(self):

        train_data=pd.read_csv(self.config.train_data_path,names=self.config.columns,sep="\s+",header=None)
        test_data=pd.read_csv(self.config.test_data_path,names=self.config.columns,sep="\s+",header=None)
        ground_truth_data=pd.read_csv(self.config.ground_truth_data_path,names=["RUL"])
        logger.info("Data loaDeD")

        print(train_data.shape)
        train_data=self.Calculate_RUL(train_data)
        logger.info(train_data["RUL"].head(2))

        logger.info("rul calcualateD")
        print(train_data.shape)

        X_train=train_data.iloc[:,:-1]
        y_train=train_data.iloc[:,-1]
        logger.info(y_train.head(2))

        X_train=self.impute_outliers(X_train)
        logger.info("outliers imputeD")

        X_train=X_train.drop(self.config.columns_to_drop,axis=1)
        
        print(X_train.shape)

        print(test_data.shape)
        test_data=test_data.groupby("Engine Number").last().reset_index().drop(columns=["Engine Number","Times/ in cycle","Burner fuel-air ratio", "Required fan speed","Total Fan inlet temperature","Total Fan inlet pressure", "Required fan conversion speed", "Mach Number(Setting_2)", "Bleed enthalpy","Engine pressure ratio(P50/P2)","TRA(Setting_3)"],axis=1)
        
        columns = list(X_train.columns[1:])

        logger.info("Data preprocessing start")
        preprocessor = ColumnTransformer(
            transformers=[
                ("Numeric", StandardScaler(), columns)
            ],
            remainder='passthrough'
        )
        preprocessor_pipeline = Pipeline(
            steps=[
                ("preprocessor", preprocessor)
            ]
        )

        cols_names = list(X_train.columns[:])

        X_train = pd.DataFrame(preprocessor_pipeline.fit_transform(X_train), columns=cols_names)
        X_test = pd.DataFrame(preprocessor_pipeline.transform(test_data), columns=cols_names)

        logger.info("Data saving process start")

        X_train.to_csv(os.path.join(self.config.root_dir, "X_train.csv"),index = False)
        y_train.to_csv(os.path.join(self.config.root_dir,"y_train.csv"),index=False)
        X_test.to_csv(os.path.join(self.config.root_dir, "X_test.csv"),index = False)
        ground_truth_data.to_csv(os.path.join(self.config.root_dir,"RUL.csv"),index=False)

        logger.info("Splited data into training and test sets")
        logger.info(X_train.shape)
        logger.info(X_test.shape)
