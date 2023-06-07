import pandas as pd
from proptables.water.import_data_water import data_path_TempSat

class saturatedwater:
    def __init__(self):
        self.Tempdata=pd.read_csv(data_path_TempSat)
        self.Tempdata=self.Tempdata.iloc[2:,-1]
    