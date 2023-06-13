from importlib import resources

def get_flatland(loc):
    """Get path to example

    Returns
    -------
    pathlib.PosixPath
        Path to file.

    References
    ----------
    """
    with resources.path("proptables.water", loc) as f:
        data_file_path = f
    return data_file_path

data_path_TempSat=get_flatland("H2O_TempSat.csv")

data_path_PresSat=get_flatland("H2O_PresSat.csv")

data_path_SuperHeat=get_flatland("H2O_Super.csv")

data_path_SuperSat=get_flatland("H2O_superSat.csv")