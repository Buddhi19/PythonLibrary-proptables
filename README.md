[![PyPI version](https://badge.fury.io/py/proptables.svg)](https://badge.fury.io/py/proptables)
[![pypi supported versions](https://img.shields.io/pypi/pyversions/proptables.svg)](https://pypi.python.org/pypi/proptables)
[![Python package](https://github.com/Buddhi19/PythonLibrary-proptables/actions/workflows/python-package.yml/badge.svg)](https://github.com/Buddhi19/PythonLibrary-proptables/actions/workflows/python-package.yml)
# Python Property Tables Library - `proptables`

`proptables` is a Python library designed to provide quick access to property tables for R134a and water, primarily aimed at engineers and researchers needing fluid property data in thermodynamic calculations.

## Features

- Provides easy-to-access property data for R134a and water.
- Useful for thermodynamics, refrigeration, and heating applications.
- Simplifies accessing and calculating fluid properties programmatically.

# proptables: User Manual

## Installation

To install the `proptables` library, run the following command in your terminal or command prompt:

```bash
pip install proptables
```

### Example Output (Google Colab):
```plaintext
Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/
Collecting proptables
  Downloading proptables-0.0.7-py3-none-any.whl (32 kB)
Installing collected packages: proptables
Successfully installed proptables-0.0.7
```

---

## Importing Components

To use the library, import the required components as follows:

```python
from proptables import R134a, water
```

---

## Using Water Tables

The `water` function can be used for various thermodynamic properties. Example usages:

### By Pressure
```python
water(Pressure=200)
```

### By Pressure and Enthalpy
```python
water(Pressure=200, Enthalpy=1500)
```

### By Temperature
```python
water(Temperature=54)
```

### By Temperature and Entropy
```python
water(Temperature=54, Entropy=5)
```

### Example with Superheated Property
```python
water(Pressure=4000, Superheated=True)
```

---

## Using R134a Tables

The `R134a` function supports similar property queries. Example usages:

### By Temperature
```python
R134a(Temperature=36)
```

### By Temperature and Enthalpy
```python
R134a(Temperature=34, Enthalpy=112)
```

### By Pressure
```python
R134a(Pressure=600)
```

### Example with Superheated Property
```python
R134a(Pressure=1200, Superheated=True)
```

---

## Data Tables

The library provides detailed thermodynamic tables for water and R134a. Below are some examples:

### Water Table (Pressure-based)
| MPa | degC | vf     | vg     | uf    | ug    | hf    | hfg    | hg    | sf     | sfg    | sg     |
|-----|-------|--------|--------|-------|-------|-------|--------|-------|--------|--------|--------|
| 25  | 0.2   | 0.001061 | 0.8857 | 504.5 | 2529.1 | 504.7 | 2201.5 | 2706.2 | 1.5302 | 5.5967 | 7.1269 |

### R134a Table (Temperature-based)
| degC | kPa   | vf     | vg     | uf    | ug    | hf    | hfg    | hg    | sf     | sfg    | sg     |
|------|-------|--------|--------|-------|-------|-------|--------|-------|--------|--------|--------|
| 31   | 36.0  | 0.00086 | 0.0224 | 101.55 | 249.1 | 102.33 | 167.17 | 269.5 | 0.3761 | 0.5407 | 0.9168 |

---

## Reporting Issues

If you encounter any errors or issues, please report them on the library's [GitHub page](https://github.com/Buddhi19/PythonLibrary-proptables).

---

# Thank you for using `proptables`!

