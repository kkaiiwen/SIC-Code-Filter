# SIC-Code-Filter

## Description

This program processes Companies House Basic Company Data CSV files and filters them by target Standard Industrial Classification (SIC) codes in Python.

The program first prompts the user to select an input folder (containing the CSV files) and an output folder (where results will be stored). It initializes a results structure in which each target SIC code has its own collection list. Each CSV file is then read into a pandas DataFrame, with relevant columns renamed for consistency. A cleaning function is applied to the SIC code fields to remove non-numeric characters and standardize values.

For each company row, the program compiles a record of its details and checks whether any of its SIC codes match the target list. Matching records are stored under the corresponding SIC code. After all files are processed, the program generates one filtered CSV file for each target SIC code with matches and saves them in the chosen output folder. It also reports which codes produced no results.

This workflow ensures the output consists of clean, targeted datasets that are ready for sector-specific analysis.


