from PredictiveMaintenance import logger
import pandas as pd
from sklearn.preprocessing import RobustScaler, MinMaxScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from PredictiveMaintenance.entity import config_entity
import os

class DataTransformation:
    def __init__(self, config: config_entity.DataTransformationConfig):
        self.config = config

    def add_RUL_feature(self, df: pd.DataFrame) -> pd.DataFrame:
        df_RUL = df.groupby("Engine Number").agg({"Times/ in cycle":"max"})
        df_RUL.rename(columns={"Times/ in cycle": "total life"}, inplace=True)
        logger.info(df_RUL.head())

        df = df.merge(df_RUL, on=["Engine Number"], how="left")
        logger.info(df.head())

        df["RUL"] = df["total life"] - df["Times/ in cycle"]
        df.drop(["total life"], axis=1, inplace=True)
        logger.info(df.head())  

        return df
    
    def train_test_split(self, df1: pd.DataFrame, df2: pd.DataFrame):
        X_train = df1.iloc[:,:-1]
        y_train = df1.iloc[:,-1]
        X_test = df2.iloc[:,:len(df2.columns)+1]

        return X_train, y_train, X_test

    def replace_outliers_with_median(self, df: pd.DataFrame) -> pd.DataFrame:
        Q1 = df.quantile(0.10) 
        Q3 = df.quantile(0.90)
        IQR = Q3 - Q1
        
        outlier_low = Q1 - 1.5 * IQR
        outlier_high = Q3 + 1.5 * IQR
        
        for col in df.columns:
            col_median = df[col].median() 
            df.loc[df[col] < outlier_low[col], col] = col_median  
            df.loc[df[col] > outlier_high[col], col] = col_median
            
        return df
    
    def prepare_test_data(self, df: pd.DataFrame) -> pd.DataFrame:
        df_cycle = df.groupby(["Engine Number"]).agg({"Times/ in cycle":"max"})
        df_cycle.rename(columns={"Times/ in cycle":"life"}, inplace=True)

        df = df.merge(df_cycle, how="left", on=["Engine Number"])

        df = df[(df["Times/ in cycle"] == df["life"])]
        df.drop(["life"], axis=1, inplace=True)

        logger.info(df.head())
        return df
    
    def do_data_transformation(self):
        train_folder_path = self.config.train_data_path
        test_folder_path = self.config.test_data_path

        dfs = {}
        for filename in os.listdir(train_folder_path):
            if filename.endswith(".txt"):
                file_path = os.path.join(train_folder_path, filename)

                df_name = os.path.splitext(filename)[0]

                df = pd.read_csv(file_path, sep="\s+", header=None, names=self.config.all_schema)

                dfs[df_name] = df

                logger.info(f"DataFrame '{df_name}' has been created with shape: {df.shape}")
        
        for filename in os.listdir(test_folder_path):
            if filename.endswith(".txt"):
                file_path = os.path.join(test_folder_path, filename)

                df_name = os.path.splitext(filename)[0]

                df = pd.read_csv(file_path, sep="\s+", header=None, names=self.config.all_schema)

                dfs[df_name] = df

                logger.info(f"DataFrame '{df_name}' has been created with shape: {df.shape}")

        train_FD001 = dfs["train_FD001"]
        test_FD001 = dfs["test_FD001"]

        logger.info("Start adding RUL features for train_FD001\n")
        train_FD001 = self.add_RUL_feature(train_FD001)
        logger.info("Finished adding RUL features for train_FD001\n")

        logger.info("Start preparing test_FD001\n") 
        test_FD001 = self.prepare_test_data(test_FD001)
        logger.info("Finished preparing test_FD001\n")    
        
        logger.info("train_test_split process started.....")
        X_train, y_train, X_test = self.train_test_split(df1=train_FD001, df2=test_FD001)
        logger.info("train_test_split completed.")

        logger.info(f"X_train: {X_train.shape}, y_train: {y_train.shape}, X_test: {X_test.shape}")
        
        logger.info("Dropping unnecessory columns.")
        logger.info(f"Before dropping: {X_train.columns}")

        X_train.drop(columns=self.config.cols_to_drop, axis=1, inplace=True)
        X_test.drop(columns=self.config.cols_to_drop, axis=1, inplace=True)

        logger.info(f"After dropping: {X_train.columns}")
        logger.info("Unnecessory columns are droped.")

        y_train = y_train.clip(upper=125)

        logger.info("Outlier dropping start")
        X_train = self.replace_outliers_with_median(X_train)
        X_test = self.replace_outliers_with_median(X_test)
        logger.info("Outlier dropping completed.")

        numerical_columns = list(X_train.columns[1:])

        logger.info("Data preprocessing start")
        preprocessor = ColumnTransformer(
            transformers=[
                ("Numeric", RobustScaler(), numerical_columns)
            ],
            remainder='passthrough'
        )
        preprocessor_pipeline = Pipeline(
            steps=[
                ("preprocessor", preprocessor)
            ]
        )

        cols_names = list(X_train.columns[1:])
        cols_names.extend(["Times/ in cycle"])

        X_train = pd.DataFrame(preprocessor_pipeline.fit_transform(X_train), columns=cols_names)
        X_test = pd.DataFrame(preprocessor_pipeline.transform(X_test), columns=cols_names)

        logger.info(X_train.head())
        logger.info(X_test.head())
        logger.info("Data preprocessing completed.")

        X_train.to_csv(os.path.join(self.config.root_dir, 'X_train.csv'), index=False)
        X_test.to_csv(os.path.join(self.config.root_dir, 'X_test.csv'), index=False)

        y_train.to_csv(os.path.join(self.config.root_dir, 'y_train.csv'), index=False)