from PredictiveMaintenance import logger
import pandas as pd
from PredictiveMaintenance.entity import config_entity

class DataValidation:
    def __init__(self, config: config_entity.DataValidationConfig):
        self.config = config

    def validate_all_columns(self)-> bool:
        try:
            validation_status = None

            index_name = ["Engine Number", "Times/ in cycle"]
            setting_name = ["Altitude(Setting_1)", "Mach Number(Setting_2)", "TRA(Setting_3)"]
            sensor_name = ["Total Fan inlet temperature", "Total LPC outlet temperature", "Total HPC outlet temperature", "Total LPT outlet temperature",
            "Total Fan inlet pressure","Total bypass-duct pressure", "Total HPC outlet pressure", "Physical fan speed", "Physical core speed","Engine pressure ratio(P50/P2)", "Static HPC outlet pressure",
            "Ratio of fuel flow to Ps30", "Corrected fan speed", "Corrected core speed", "Bypass Ratio", "Burner fuel-air ratio", "Bleed enthalpy", "Required fan speed", "Required fan conversion speed",
            "HPT coolant bleed", "LPT coolant bleed"]

            columns_name = index_name + setting_name + sensor_name

            data = pd.read_csv(self.config.unzip_file_dir, sep="\s+", header=None, names=columns_name)
            
            all_cols = list(data.columns)

            all_schema = self.config.all_schema.keys()
            
            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
                
            return validation_status
        
        except Exception as e:
            raise e