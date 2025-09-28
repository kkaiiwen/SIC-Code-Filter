# SIC-Code-Filter

## Description

This program processes Companies House Basic Company Data CSV files and filters them by target Standard Industrial Classification (SIC) codes in Python. 

The program begins by prompting the user to select both the input folder (containing the CSV files) and the output folder (where the results will be stored). It then prepares a results structure where each target SIC code has its own storage list. Next, it loops through every CSV file in the input folder, reading the data into a pandas DataFrame and renaming the necessary columns for consistency. A cleaning function is applied to each SIC code field to strip away any extra characters and keep only the numeric part. For each company row, the program builds a record of its details and checks whether any of its SIC codes match the target list. If so, that record is added to the correct results group. Once all files are processed, the program saves one filtered CSV file for each target code that has matches in the output folder selected at the start, while also reporting which codes had no results. This ensures the output consists of clean, targeted datasets that are ready for analysis within specific sectors.


