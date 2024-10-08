#!/usr/bin/env python
# coding: utf-8

# import libraries
import pandas as pd
import os

#This code converts Excel file to CSV 
excel_file_path = 'first_excel_file.xlsx'  # Replace with your Excel file path
csv_file_path = 'desired_name.csv'  # Change this to your desired output file path

# Check if the CSV file already exists; if not, convert the Excel file to CSV
if not os.path.isfile(csv_file_path):
    df = pd.read_excel(excel_file_path, sheet_name=None)  # Read all sheets into a dictionary

# Combine all sheets into a single DataFrame
    combined_df = pd.concat(df.values(), ignore_index=True)

    # Save the combined DataFrame as a CSV file
    combined_df.to_csv(csv_file_path, index=False)

# This code reads newly-created CSV file, finds duplicates and creates a new CSV file.
df = pd.read_csv('second_file.csv',dtype={'Email Address': str},low_memory=False)

# Create an empty list to store rows with duplicate emails
duplicate_email_rows = []

# Identify duplicate email addresses within the DataFrame
duplicates = df[df['Email Address'].duplicated()]

# Append entire rows with duplicate emails to the list
duplicate_email_rows.extend(duplicates.to_dict('records'))
duplicate_email_df = pd.DataFrame(duplicate_email_rows)
duplicate_email_df.to_csv('duplicate_emails_in_same_file.csv', index=False)


#This code converts second Excel file to CSV 
excel_file_path = 'second_file.xlsx'  # Replace with the path to your Excel file

# Define the output CSV file path
csv_file_path = 'second_file.csv'  # Change this to your desired output file path

# Initialize an empty list to store DataFrames
all_dataframes = []

# Create an ExcelFile object
xls = pd.ExcelFile(excel_file_path)

# Iterate over each sheet in the Excel file
for sheet_name in xls.sheet_names:
    # Read the sheet into a DataFrame
    df_1 = pd.read_excel(excel_file_path, sheet_name=sheet_name,header=None, squeeze=True)
    all_dataframes.append(df_1)

# Concatenate all DataFrames into a single DataFrame
combined_df_master = pd.concat(all_dataframes, ignore_index=True)

# Save the combined DataFrame as a CSV file
combined_df_master.to_csv(csv_file_path, index=False)


--------------------------------------------------------------------------------------------------------------------------------------------------------

#This code reads 2 CSV files and then compares the email addresses and then creates a new file.

sg_emails_df = pd.read_csv('first_file.csv',dtype={'Email Address': str},low_memory=False) #change the variable name as per your file
master_emails_df = pd.read_csv('second_file.csv',dtype={'Email': str},low_memory=False) #change the variable name as per your file

# Extract the 'Email Address' column from each DataFrame
sg_emails = sg_emails_df['Email Address']
master_emails = master_emails_df['Email']

# Find common email addresses between the two DataFrames
common_emails = sg_emails[sg_emails.isin(master_emails)]

# Create a DataFrame with the common email addresses
common_emails_df = pd.DataFrame({'Common Email': common_emails})
common_emails_df.to_csv('duplicate_emails_in_master_file.csv', index=False)

# Check if 'abc@example.com' exists in the 'Email' column of second file
email_to_check = 'abc@example.com'
is_present=  master_emails_df['Email'].isin([email_to_check]).any()

if is_present:
    print(f"{email_to_check} exists in master file.")
else:
    print(f"{email_to_check} does not exist in master file.")
