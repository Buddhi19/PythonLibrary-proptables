import pandas as pd

class R134a:
    def __init__(self):
        self.dfPressure=pd.read_csv("./R134a_PresSat.csv")
        self.dfTemperature=pd.read_csv("./R134a_TempSat.csv")



    def FindbyTemp(self,Temperature):
        if Temperature in self.dfTemperature["degC"].unique():
            indexing=self.dfTemperature[self.dfTemperature["degC"]==Temperature].index.values
            row=self.dfTemperature.iloc[indexing]
            return row
        else:
            nearest=self.dfTemperature["degC"].sub(Temperature).abs().argsort()[:2]
            result=self.dfTemperature.iloc[nearest]
            result.loc[-1,"degC"]=Temperature
            result =result.sort_values(by='degC')
            result=result.reset_index(drop=True)
            result.set_index('degC', inplace=True)
            result.interpolate(method='index', inplace=True)
            result.reset_index(inplace=True)
            return result
            


    def FindbyPressure(self,Pressure):
        if Pressure in self.dfPressure["kPa"].unique():
            indexing=self.dfPressure[self.dfPressure["kPa"]==Pressure].index.values
            row=self.dfPressure.iloc[indexing]
            return row
        else:
            nearest=self.dfPressure["kPa"].sub(Pressure).abs().argsort()[:2]
            result=self.dfPressure.iloc[nearest]
            result.loc[-1,"kPa"]=Pressure
            result =result.sort_values(by='kPa')
            result=result.reset_index(drop=True)
            result.set_index('kPa', inplace=True)
            result.interpolate(method='index', inplace=True)
            result.reset_index(inplace=True)
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


    def values(self,Temperature=None,Pressure=None,Enthalpy=None,Superheated=None):
        if Temperature and Pressure:
            return
        if Temperature and Enthalpy:
            print(self.calculate_x_temp(Temperature,Enthalpy))
            return
        if Pressure and Enthalpy:
            print(self.calculate_x_pressure(Pressure,Enthalpy))
            return
        if Temperature:
                print(self.FindbyTemp(Temperature))
            
        if Pressure:
                print(self.FindbyPressure(Pressure))





r=R134a()
# r.values(Temperature=55)
# r.values(Temperature=55,Pressure=344)
r.values(Temperature=32,Enthalpy=344)