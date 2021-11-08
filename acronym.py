import pandas as pd
import glob


# Two-character acronym to organization acronym map
acronyms = {
    # USDA Mission Area
    "DA": "DA",
    "DM": "DM",
    "FP": "FPAC",
    "NU": "FNCS",
    "FD": "FOSA",
    "MR": "MRP",
    "NR": "NRE",
    "RE": "REE",
    "RU": "RUDV",
    "TF": "TFAA",
    # USDA Agencies
    "MS": "AMS",
    "RS": "ARS",
    "AP": "APHIS",
    "ER": "ERS",
    "SA": "FSA",
    "FN": "FNS",
    "SI": "FSIS",
    "FA": "FAS",
    "FS": "FS",
    "GI": "GIPSA",
    "AS": "NASS",
    "IF": "NIFA",
    "RC": "NRCS",
    "RM": "RMA",
    "RD": "RD",
    # USDA Offices
    "BP": "OBPA",
    "OC": "OC",
    "CM": "OCM",
    "OE": "OE",
    "HA": "OHA",
    "HS": "OHS",
    "HR": "OHRM",
    "OO": "OO",
    "PF": "OPFM",
    "PE": "OPPE",
    "CP": "OCP",
    "SP": "OSSP",
    "SB": "OSDBU",
    "CR": "OASCR",
    "CE": "OCE",
    "FO": "OCFO",
    "FC": "NFC",
    "IO": "OCIO",
    "ES": "OES",
    "GC": "OGC",
    "IG": "OIG",
    "SE": "OSEC",
    # USDA Support Organizations
    "TC": "DISC",
    "AG": "AG",
}

# This creates an empty dataframe, expect column 'System Name'
data = pd.DataFrame(columns=['System Name'])

# The relative filepath is where the files are located on your device
file_paths = glob.glob('./input/*.xlsx')

print("Reading in data...")
for filepath in file_paths:
    print("Reading " + filepath)
    data = data.append(pd.read_excel(filepath))
print('Data read completed.')

print("Converting acronyms...")

# Case 1: System name starts with A, but acronym is not matched (default)
data["Organization"] = "Acronym not matched"

# Case 2: System name does not start with A
data.loc[~data["System Name"].str.upper().str.startswith('A', na=False), "Organization"] = "Non-Standard naming convention"

# Case 3: System name starts with A, and acronym is matched
for acronym in acronyms:
    data.loc[data["System Name"].str.upper().str.startswith('A' + acronym, na=False), "Organization"] = acronyms[acronym]

data.to_excel('./data/data_with_acronyms.xlsx', index=False)

print("Acronym conversion completed.")
