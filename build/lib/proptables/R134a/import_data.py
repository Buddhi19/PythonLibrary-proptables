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
    with resources.path("proptables.R134a", loc) as f:
        data_file_path = f
    return data_file_path

data_path_Super=get_flatland("R134a_Super.csv")

data_path_PresSat=get_flatland("R134a_PresSat.csv")

data_path_SupPreSat=get_flatland("R134a_SupPreSat.csv")

data_path_TempSat=get_flatland("R134a_TempSat.csv")

# print(pd.read_csv(data_path_Super))