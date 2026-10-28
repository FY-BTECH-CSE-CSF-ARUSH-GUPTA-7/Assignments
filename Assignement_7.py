import pandas as pd

df = pd.read_csv(r'c:\Users\arush\Downloads\vs\sample_data_assignment_07.csv')


# Display dataset
print("Original Dataset:")
print(df)

# First 5 rows
print("\nFirst 5 Rows:")
print(df.head())

# Dataset information
print("\nDataset Info:")
print(df.info())

# Statistical summary
print("\nDescription:")
print(df.describe())

# Check missing values
print("\nMissing Values:")
print(df.isnull())

# Count missing values column-wise
print("\nMissing Values Count:")
print(df.isnull().sum())

# Fill missing values with 0
df_filled = df.fillna(0)

print("\nAfter fillna():")
print(df_filled)

# Remove rows having missing values
df_dropna = df.dropna()

print("\nAfter dropna():")
print(df_dropna)

# Check duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated())

# Remove duplicate rows
df_nodup = df.drop_duplicates()

print("\nAfter drop_duplicates():")
print(df_nodup)

# Select specific columns
print("\nName and Marks Columns:")
print(df[["Student", "Attendance"]])

# Using loc[]
print("\nFirst Row:")
print(df.loc[0])

print("\nRows 0 to 2:")
print(df.loc[0:2])

print("\nMarks Column:")
print(df.loc[:, "Attendance"])
