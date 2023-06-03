import pandas as pd
from calSuperHeatData import HeatedCal
from calSatData import SatData

def R134a(Temperature=None,Pressure=None,Enthalpy=None,Entropy=None,specificvolume=None,Superheated=None):
    
    if Temperature and Pressure:
        return HeatedCal.findsuperTemp(Pressure,Temperature)
    
    if Superheated and Pressure and Enthalpy:
        return HeatedCal.findsuperEnthalpy(Pressure,Enthalpy)
    
    if Superheated and Pressure and Entropy:
        return HeatedCal.findsuperEntropy(Pressure,Entropy)
    
    if Superheated and Pressure and specificvolume:
        return HeatedCal.findsuperspecificvolume(Pressure,specificvolume)
    
    if Superheated and Pressure:
        return HeatedCal.superheatedTable(Pressure)
    
    if Temperature and Enthalpy:
        return(SatData.calculate_x_temp(Temperature,Enthalpy))
        
    if Pressure and Enthalpy:
        return(SatData.calculate_x_pressure(Pressure,Enthalpy))
        
    if Temperature:
        return(SatData.FindbyTemp(Temperature))
        
    if Pressure:
        return(SatData.FindbyPressure(Pressure))

