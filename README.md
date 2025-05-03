# Automation_GDSC

## Data Load
```python
from dataloader import load_gdsc, prepare_features, split_data
excluded_columns = ['LN_IC50', 'AUC', 'Z_SCORE', 'DRUG_ID', 'COSMIC_ID', 'DRUG_NAME', 'CELL_LINE_NAME']
df = load_gdsc(excluded_columns=excluded_columns)   # With Drop NaN & Exclude Outlier with IQR

# Create dummy variables for categorical features and split the data into training and testing sets with default test size of 0.2
X_dummy, y = prepare_features(df, encode_dummies=True)
X_label, _ = prepare_features(df, encode_dummies=False)
Xd_tr, Xd_te, Xl_tr, Xl_te, y_tr, y_te = split_data(X_dummy, X_label, y) 
# Xd: X features with dummy variables
# Xl: X features with label encoding (e.g. Turn R, G, B into 0, 1, 2)
```

## Files
- `dataloader.py`: Contains functions to load the GDSC dataset, prepare features, and split the data into training and testing sets.
- `data.ipynb`, `exploration.ipynb`: Jupyter notebooks for data exploration and analysis.
- `main_classificication.ipynb`: Jupyter notebook for classification tasks.
- `main_regression.ipynb`: Jupyter notebook for regression tasks.
- `nn_*.ipynb`: Jupyter notebooks for neural network tasks.