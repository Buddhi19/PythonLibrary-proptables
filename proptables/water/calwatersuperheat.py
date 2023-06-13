import pandas as pd
from proptables.water.superheated import superheatedtable

class HeatedCalculater:
    def __init__(self):
        pass

    def superheatedTable(self,Pressure):
        return superheatedtable(Pressure)

    def findsuperTemp(self,Pressure,Temperature):
        ans=superheatedtable(Pressure)
        if Temperature in ans["Temp"].values:
            indexing=ans[ans["Temp"].values==Temperature].index.values
            row=ans.iloc[indexing]
            return row
        else:
            nearest=ans["Temp"].sub(Temperature).abs().argsort()[:2]
            result=ans.iloc[nearest]
            result=result.copy()
            result.loc[-1,"Temp"]=Temperature
            result =result.sort_values(by='Temp')
            result=result.reset_index(drop=True)
            result.set_index('Temp', inplace=True)
            result.interpolate(method='index', inplace=True)
            result.reset_index(inplace=True)
            result.drop([0],inplace=True)
            result=result.reset_index(drop=True)
            result.drop([1],inplace=True)
            result=result.reset_index(drop=True)
            return result
        
    def findsuperEnthalpy(self,Pressure,Enthalpy):
        ans=superheatedtable(Pressure)
        if Enthalpy in ans["enthalpy"].values:
            indexing=ans[ans["enthalpy"].values==Enthalpy].index.values
            row=ans.iloc[indexing]
            return row
        else:
            nearest=ans["enthalpy"].sub(Enthalpy).abs().argsort()[:2]
            result=ans.iloc[nearest]
            result=result.copy()
            result.loc[-1,"enthalpy"]=Enthalpy
            result =result.sort_values(by='enthalpy')
            result=result.reset_index(drop=True)
            result.set_index('enthalpy', inplace=True)
            result.interpolate(method='index', inplace=True)
            result.reset_index(inplace=True)
            result.drop([0],inplace=True)
            result=result.reset_index(drop=True)
            result.drop([1],inplace=True)
            result=result.reset_index(drop=True)
            return result
    
    def findsuperEntropy(self,Pressure,Entropy):
        ans=superheatedtable(Pressure)
        if Entropy in ans["entropy"].values:
            indexing=ans[ans["entropy"].values==Entropy].index.values
            row=ans.iloc[indexing]
            return row
        else:
            nearest=ans["entropy"].sub(Entropy).abs().argsort()[:2]
            result=ans.iloc[nearest]
            result=result.copy()
            result.loc[-1,"entropy"]=Entropy
            result =result.sort_values(by='entropy')
            result=result.reset_index(drop=True)
            result.set_index('entropy', inplace=True)
            result.interpolate(method='index', inplace=True)
            result.reset_index(inplace=True)
            result.drop([0],inplace=True)
            result=result.reset_index(drop=True)
            result.drop([1],inplace=True)
            result=result.reset_index(drop=True)
            return result
        
    def findsuperspecificvolume(self,Pressure,specificvolume):
        ans=superheatedtable(Pressure)
        if specificvolume in ans["v"].values:
            indexing=ans[ans["v"].values==specificvolume].index.values
            row=ans.iloc[indexing]
            return row
        else:
            nearest=ans["v"].sub(specificvolume).abs().argsort()[:2]
            result=ans.iloc[nearest]
            result=result.copy()
            result.loc[-1,"v"]=specificvolume
            result =result.sort_values(by='v')
            result=result.reset_index(drop=True)
            result.set_index('v', inplace=True)
            result.interpolate(method='index', inplace=True)
            result.reset_index(inplace=True)
            result.drop([0],inplace=True)
            result=result.reset_index(drop=True)
            result.drop([1],inplace=True)
            result=result.reset_index(drop=True)
            return result
        
steam=HeatedCalculater()