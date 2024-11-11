[![PyPI version](https://badge.fury.io/py/proptables.svg)](https://badge.fury.io/py/proptables)
[![pypi supported versions](https://img.shields.io/pypi/pyversions/proptables.svg)](https://pypi.python.org/pypi/proptables)
[![Python package](https://github.com/Buddhi19/PythonLibrary-proptables/actions/workflows/python-package.yml/badge.svg)](https://github.com/Buddhi19/PythonLibrary-proptables/actions/workflows/python-package.yml)
# Python Property Tables Library - `proptables`

`proptables` is a Python library designed to provide quick access to property tables for R134a and water, primarily aimed at engineers and researchers needing fluid property data in thermodynamic calculations.

## Features

- Provides easy-to-access property data for R134a and water.
- Useful for thermodynamics, refrigeration, and heating applications.
- Simplifies accessing and calculating fluid properties programmatically.

# To Install
```bash
pip install proptables
```
## How to use
```python
from proptables import R134a,water
```
## Usage

### Basic Usage
Import the library

```python
from proptables import R134a, water

data = r134a.temperature(Temperature=None,Pressure=None,
          Enthalpy=None,Entropy=None,
          specificvolume=None,Superheated=None,Compressed=None)  # Mention the values as needed to obtain the dataframe with all details



data = water.enthalpy(Temperature=None,Pressure=None,
          Enthalpy=None,Entropy=None,
          specificvolume=None,Superheated=None,Compressed=None) 
```

