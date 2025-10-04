import pandas as pd
import re
import glob
import os
import sys
import tkinter as tk
from tkinter import filedialog

# Target SIC codes
target_sic_codes = [ "41201", "41202", "42990", "43390", "43999", "43290", 
                    "25620", "71111", "41100", "71122", "68201" ]

# Select input folder with GUI
root = tk.Tk()
root.withdraw()
input_folder = filedialog.askdirectory(title = "Select folder containing CSV files")
if not input_folder:
    print("No input folder selected, exiting.")
    sys.exit()

# Select folder to save filtered results with GUI
output_folder = filedialog.askdirectory(title = "Select folder to save filtered results")
if not output_folder:
    print("No output folder selected, exiting.")
    sys.exit()
root.destroy()

# Collect CSV files
csv_files = glob.glob(os.path.join(input_folder, "*.csv"))
if not csv_files:
    print("No CSV files found in the selected folder.")
    sys.exit()

# Function to clean SIC field, keep digits only
def clean_sic(value):
    if pd.isna(value):
        return ""
    match = re.search(r"\d+", str(value))
    if match:
        return match.group(0)
    else:
        return ""

# Creates a dictionary for each target SIC code
results_by_code = {code: [] for code in target_sic_codes}

# Process all CSV files
for file_path in csv_files:
    print(f"Processing {os.path.basename(file_path)} ...")
    df = pd.read_csv(file_path, dtype = str)

    # Rename columns, skip file if layout unexpected
    try:
        df = df.rename(columns = {
            df.columns[0]: "Company Name",      # Column A
            df.columns[1]: "Company Number",    # Column B
            df.columns[26]: "SIC Code 1",       # Column AA
            df.columns[27]: "SIC Code 2",       # Column AB
            df.columns[28]: "SIC Code 3",       # Column AC
            df.columns[29]: "SIC Code 4"        # Column AD
        })
    except IndexError:
        print(f"Skipping {os.path.basename(file_path)}: unexpected column layout.")
        continue

    # Clean SIC columns
    for col in ["SIC Code 1", "SIC Code 2", "SIC Code 3", "SIC Code 4"]:
        df[col] = df[col].apply(clean_sic)

    # For each row, check if it contains each target SIC code
    for _, row in df.iterrows():
        company_data = {
            "Company Name": row["Company Name"],
            "Company Number": row["Company Number"],
            "SIC Code 1": row["SIC Code 1"],
            "SIC Code 2": row["SIC Code 2"],
            "SIC Code 3": row["SIC Code 3"],
            "SIC Code 4": row["SIC Code 4"],
            "Source File": os.path.basename(file_path)
        }
        row_codes = {row["SIC Code 1"], row["SIC Code 2"], row["SIC Code 3"], row["SIC Code 4"]}
        for code in target_sic_codes:
            if code in row_codes:
                results_by_code[code].append(company_data)

# Save the filtered files
for code, rows in results_by_code.items():
    if rows:  # only save if there are matches
        output_path = os.path.join(output_folder, f"filtered_{code}.csv")
        pd.DataFrame(rows).to_csv(output_path, index = False)
        print(f"Saved {output_path} with {len(rows)} companies.")
    else:
        print(f"No companies found with SIC {code}.")
