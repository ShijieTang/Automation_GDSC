import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import kagglehub
import os
import warnings

warnings.filterwarnings("ignore")


# ----Download from Kaggle or load preprocessed data----
current_path = None
if not current_path:
    path = kagglehub.dataset_download("samiraalipour/genomics-of-drug-sensitivity-in-cancer-gdsc")

    # Load datasets
    gdsc_dataset = pd.read_csv(os.path.join(path, 'GDSC_DATASET.csv'))
    compounds_annotation = pd.read_csv(os.path.join(path, 'Compounds-annotation.csv'))
    gdsc2_dataset = pd.read_csv(os.path.join(path, 'GDSC2-dataset.csv'))
    cell_lines_details = pd.read_excel(os.path.join(path, 'Cell_Lines_Details.xlsx'))

print("Path to dataset files:", path)


# ----GDSC Dataset----
gdsc_df_clean = gdsc_dataset.dropna(subset=['TARGET'])

gdsc_df_clean['Cancer Type (matching TCGA label)'].fillna(gdsc_df_clean['Cancer Type (matching TCGA label)'].mode()[0], inplace=True)
gdsc_df_clean['Microsatellite instability Status (MSI)'].fillna(gdsc_df_clean['Microsatellite instability Status (MSI)'].mode()[0], inplace=True)

# Cap outliers in LN_IC50 using IQR method (Winsorization)
Q1 = gdsc_df_clean['LN_IC50'].quantile(0.25)
Q3 = gdsc_df_clean['LN_IC50'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

gdsc_df_clean['LN_IC50'] = gdsc_df_clean['LN_IC50'].clip(lower=lower_bound, upper=upper_bound)


# ----save the cleaned dataset----
gdsc_df_clean.to_csv(os.path.join(path, 'GDSC_Cleaned.csv'), index=False)
print(f"Cleaned dataset saved to {os.path.join(path, 'GDSC_Cleaned.csv')}")