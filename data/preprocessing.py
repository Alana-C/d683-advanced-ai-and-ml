# PREPROCESSING DATA
import pandas as pd
import numpy as np
from user_interface import *

# B1. The following preprocessing techniques have been applied:
# - converting categorical variables into intervals
# - cleaning data
# - checking for invalid data

# Importing Unprocessed Data
df = pd.read_csv('original_mushrooms.csv')
translations = get_translations('category_translations.txt')

# converting categorical variables to numbers
for column in df.columns:
    df[column] = df[column].astype('category')
    df[column] = df[column].map(translations[column])
    # print(df.head()[column].map(translations[column]), "\n")
    # table = pd.crosstab(df['class'], df[column].map(translations[column]), normalize='all')
    # print(table)

df['class'].astype('boolean')
df['bruises'].astype('boolean')

df.to_csv('mushrooms.csv', index=False)
