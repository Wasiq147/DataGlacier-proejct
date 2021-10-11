import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Store the paths to the two files containing the data
path_train = 'drive/MyDrive/Cross Selling/Train.csv'
path_test = 'drive/MyDrive/Cross Selling/Test.csv'

# Load the data into two data frames containing the data from each file
df1 = pd.read_csv(path_train, header=0)
df2 = pd.read_csv(path_test, header=0)

# Combine (not join) the data frames
df = pd.concat([df1, df2], axis=0)
#%%
# Print the number of missing values for each variable
df2.isna().sum()
#%%
# The following command returns an empty data frame
df[df['indrel'] == 99][df['ult_fec_cli_1t'].isna()]
# This is because where the value of indrel is 1 the variable 'ult_fec_cli_1t'
# can have no value by its definition, and so it really has no missing values.

# Next we consider the variables indrel_1mes and tiprel_1mes
df[df["indrel_1mes"].isna()]
df[df["tiprel_1mes"].isna()]
# and impute their modes for their missing values
df['indrel_1mes'].fillna(df['indrel_1mes'].mode()[0], inplace = True)
df['tiprel_1mes'].fillna(df['tiprel_1mes'].mode()[0], inplace = True)

# We impute the variable for income simply using the overall mean
df['renta'].fillna(df['renta'].mean(), inplace = True)

# Looking the sex variable, the missing values could represent people who
# refused to declare their gender or who don't identify as either male or
# female. It is better not to impute but simply to label these observations X
df['sexo'].fillna('X', inplace = True)

# Considering missing values of the variable conyuemp indicating marriages
# between customers and employees:
df[df['conyuemp'] == 'S']
# There is a large number of missing values just in the test data, but of the
# non-missing values, the customers who are spouses of employees appear to be
# extremely uncommon (only 1 in the test data), so we impute the mode value to this variable
df['conyuemp'].fillna(df['conyuemp'].mode()[0], inplace = True)

# For the small number of missing values in the categorical variable
# canal_entrada we use mode imputation again
df['canal_entrada'].fillna(df['canal_entrada'].mode()[0], inplace = True)

# For the cod_prov and nomprov variables, simple imputation of the modes would
# be inappropriate and we use hot-deck imputation in this case
df.fillna(method='ffill', inplace=True)
df2[df2['segmento'] == '01 - TOP']