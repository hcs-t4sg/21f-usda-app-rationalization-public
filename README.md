## Setup and running the code
The acronym conversion algorithm can be found in `acronym.py`.

Install Python 3.9 (or latest version).

Use `pip` (built-in Python package management system) or another library to install the following libraries: 
- Pandas: run `pip install pandas`, see https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html
- openpyxl: run `pip install openpyxl`, see https://openpyxl.readthedocs.io/en/stable/#installation

The Excel files are expected to be stored in the `input/` folder of the project directory. This can also be changed to a directory of choice by updating the filepath in line 66 of `acronym.py`.

After installing all of the required packages, go to your Terminal and navigate to the directory where the script is held. Then, type `python acronym.py` into your Terminal.

The script will then perform the acronym conversion and output the resulting Excel file to `data/data_with_acronyms.xlsx`.
