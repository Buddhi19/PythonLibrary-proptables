from proptables.water.calwatersat import SatwaterCal
from proptables.water.calwatersuperheat import steam

def water(Temperature=None,Pressure=None,
          Enthalpy=None,Entropy=None,
          specificvolume=None,Superheated=None,Compressed=None):

    if Temperature and Pressure:
        return steam.findsuperTemp(Pressure,Temperature)
    
    if Superheated and Pressure and Enthalpy:
        return steam.findsuperEnthalpy(Pressure,Enthalpy)
    
    if Superheated and Pressure and Entropy:
        return steam.findsuperEntropy(Pressure,Entropy)
    
    if Superheated and Pressure and specificvolume:
        return steam.findsuperspecificvolume(Pressure,specificvolume)
    
    if Superheated and Pressure:
        return steam.superheatedTable(Pressure) 

    if Temperature and Enthalpy:
        return(SatwaterCal.calculate_x_temp(Temperature,Enthalpy))

    if Pressure and Enthalpy:
        return(SatwaterCal.calculate_x_pressure(Pressure,Enthalpy))

    if Pressure and Entropy:
        return(SatwaterCal.calculate_x_pressure_entropy(Pressure,Entropy))

    if Temperature and Entropy:
        return(SatwaterCal.calculate_x_temp_entropy(Temperature,Entropy))
    
    if Temperature:
        return(SatwaterCal.FindbyTemp(Temperature))
    
    if Pressure:
        return(SatwaterCal.FindbyPressure(Pressure))

    
