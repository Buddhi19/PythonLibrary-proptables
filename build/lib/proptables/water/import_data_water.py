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