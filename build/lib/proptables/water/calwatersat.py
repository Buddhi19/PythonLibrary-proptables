import pandas as pd
from proptables.water.import_data_water import data_path_TempSat,data_path_PresSat

class saturatedwater:
    def __init__(self):
        self.Tempdata=pd.read_csv(data_path_TempSat)
        self.Tempdata=self.Tempdata.iloc[:,:-1]
        self.Presdata=pd.read_csv(data_path_PresSat)
        self.Presdata=self.Presdata.iloc[:,:-1]

    def FindbyTemp(self,Temperature):
        if Temperature in self.Tempdata["degC"].unique():
            indexing=self.Tempdata[self.Tempdata["degC"]==Temperature].index.values
            row=self.Tempdata.iloc[indexing]
            return row
        else:
            nearest=self.Tempdata["degC"].sub(Temperature).abs().argsort()[:2]
            result=self.Tempdata.iloc[nearest]
            result=result.copy()
            result.loc[-1,"degC"]=Temperature
            result =result.sort_values(by='degC')
            result=result.reset_index(drop=True)
            result.set_index('degC', inplace=True)
            result.interpolate(method='index', inplace=True)
            result.reset_index(inplace=True)
            result.drop([0],inplace=True)
            result=result.reset_index(drop=True)
            result.drop([1],inplace=True)
            result=result.reset_index(drop=True)
            return result
        
    def FindbyPressure(self,Pressure):
        Pressure=float(Pressure)*0.001
        if Pressure in self.Presdata["MPa"].unique():
            indexing=self.Presdata[self.Presdata["MPa"]==Pressure].index.values
            row=self.Presdata.iloc[indexing]
            return row
        else:
            nearest=self.Presdata["MPa"].sub(Pressure).abs().argsort()[:2]
            result=self.Presdata.iloc[nearest]
            result=result.copy()
            result.loc[-1,"MPa"]=Pressure
            result =result.sort_values(by='MPa')
            result=result.reset_index(drop=True)
            result.set_index('MPa', inplace=True)
            result.interpolate(method='index', inplace=True)
            result.reset_index(inplace=True)
            result.drop([0],inplace=True)
            result=result.reset_index(drop=True)
            result.drop([1],inplace=True)
            result=result.reset_index(drop=True)
            return result
        
    def calculate_x_temp(self,Temperature,Enthalpy):
        result=self.FindbyTemp(Temperature)
        result=pd.DataFrame(result)
        if result.shape[0]==3:        
            result.drop([0],inplace=True)
            result=result.reset_index(drop=True)
            result.drop([1],inplace=True)
            result=result.reset_index(drop=True)
        Hf=result.iat[0,6]
        Hg=result.iat[0,8]
        x=(Enthalpy-Hf)/Hg
        result["x"]=x
        return result
    
    def calculate_x_pressure(self,Pressure,Enthalpy):
        result=self.FindbyPressure(Pressure)
        result=pd.DataFrame(result)
        if result.shape[0]==3:        
            result.drop([0],inplace=True)
            result=result.reset_index(drop=True)
            result.drop([1],inplace=True)
            result=result.reset_index(drop=True)
        Hf=result.iat[0,6]
        Hg=result.iat[0,8]
        x=(Enthalpy-Hf)/Hg
        result["x"]=x
        return result

    ############################################################# version 0.0.3 ##################################

    def calculate_x_temp_entropy(self,Temperature,Entropy):
        result=self.FindbyTemp(Temperature)
        result=pd.DataFrame(result)
        if result.shape[0]==3:        
            result.drop([0],inplace=True)
            result=result.reset_index(drop=True)
            result.drop([1],inplace=True)
            result=result.reset_index(drop=True)
        Sf=result.iat[0,9]
        Sg=result.iat[0,10]
        x=(Entropy-Sf)/Sg
        result["x"]=x
        return result
    
    def calculate_x_pressure_entropy(self,Pressure,Entropy):
        result=self.FindbyPressure(Pressure)
        result=pd.DataFrame(result)
        if result.shape[0]==3:        
            result.drop([0],inplace=True)
            result=result.reset_index(drop=True)
            result.drop([1],inplace=True)
            result=result.reset_index(drop=True)
        Sf=result.iat[0,9]
        Sg=result.iat[0,10]
        x=(Entropy-Sf)/Sg
        result["x"]=x
        return result

SatwaterCal=saturatedwater()
    