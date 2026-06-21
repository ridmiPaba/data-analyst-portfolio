# Day 1 - Superstore Sales Analysis - Python
# Objective: Same 3 objectives as Excel and MySQL

import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('/Users/prabhavihemachandra/Desktop/Day1_Project/Sample - Superstore.csv', encoding='latin1')

# Checking loaded data

print("Total rows:", len(df))
print("Total columns:", len(df.columns))
print("\nFirst 5 rows:")
print(df.head())

# ================================================
# QUALITY CHECKS
# ================================================


# Check 1 - Column Names

print("Column Names:")
print(df.columns.to_list())

# Check 2 - Missing values
print("\n" + "=" * 20)
print("Checking missing values")
print(df.isnull().sum())

# Check 3 - Duplicate  values
print("\n" + "=" * 20)
print("Total duplicate rows:")
print(df.duplicated().sum())

# Check 4 - Inconsistent Text
print("\n" + "=" * 20)
print("Checking inconsistent in text in values")
print("Unique Categories: ",  df['Category'].unique())
print("Unique Regions: ",  df['Region'].unique())
print("Unique Segments: ",  df['Segment'].unique())
print("Unique Ship Modes: ",  df['Ship Mode'].unique())

# Check 5 - Cheking extra spaces
print("\n" + "=" * 20)
print("Checking extra spaces")
category_spaces = df["Category"].str.strip() != df["Category"]
region_spaces = df["Region"].str.strip() != df["Region"]
print("Extra spaces in Category: " , category_spaces.sum())
print("Extra spaces in Region: " , region_spaces.sum())


# Check 6 - Checking Date format
print("\n" + "=" * 20)
print("Checking Date format")
print("Order date data type: ", df["Order Date"].dtype)
print("Sample dates: ", df["Order Date"].head(3).to_list())

df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

print("Order date data type: ", df["Order Date"].dtype)