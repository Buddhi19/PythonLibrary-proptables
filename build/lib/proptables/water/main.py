from proptables.water.calwatersat import SatwaterCal

def water(Temperature=None,Pressure=None,
          Enthalpy=None,Entropy=None,
          specificvolume=None,Superheated=None,Compressed=None):

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

    
