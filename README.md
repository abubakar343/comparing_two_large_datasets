# Excel to CSV Conversion and Duplicate Email Detection

This project is designed to handle large datasets in Excel files, such as those with millions of rows, by converting them to CSV format for easier processing. It includes functionality for identifying duplicate entries within a dataset and comparing two datasets to find common entries. The code was developed with the help of [Pandas documentation](https://pandas.pydata.org/docs/).

## Features

1. **Excel to CSV Conversion**: 
   - Converts large Excel files to CSV format, making data manipulation more efficient.
   - Combines multiple sheets from an Excel file into a single CSV file.

2. **Duplicate Email Detection within a Dataset**:
   - Identifies duplicate email addresses within a CSV file and saves the results in a new CSV file.

3. **Comparison of Two Datasets**:
   - Compares email addresses from two different CSV files to find common entries.
   - Outputs the common email addresses into a new CSV file.

## Installation

Ensure you have Python installed, along with the required libraries. You can install the necessary libraries using pip:

```bash
pip install pandas
```

## Usage

1. **Convert Excel to CSV**:
   - Place your Excel file in the same directory as the script.
   - Set the `excel_file_path` variable to your file's name.
   - Run the script to convert the Excel file to a CSV file.

2. **Find Duplicates within a CSV File**:
   - The script reads a CSV file and identifies any duplicate email addresses.
   - The duplicate entries are saved to a new CSV file.

3. **Compare Two CSV Files for Duplicate Emails**:
   - The script reads two CSV files and compares their email addresses.
   - Common email addresses are saved to a new CSV file.
   - You can also check if a specific email exists in one of the datasets.

## Notes

- The code is designed to handle large datasets efficiently.
- Ensure your input files are in the correct format and path specified in the script.
