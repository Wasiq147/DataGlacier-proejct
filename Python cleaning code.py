import pandas as pd

df = pd.read_csv (r'/content/drive/MyDrive/Test.csv', header=0)
df.dropna(subset = ["ind_empleado"], inplace=True) #remove rows with blank entries in Employee Index
df.dropna(subset = ["canal_entrada"], inplace=True) #remove rows with blank entries in Channels Used by Customers to Join
df.dropna(subset = ["cod_prov"], inplace=True) #remove rows with blank entries in Province Code
df.dropna(subset = ["segmento"], inplace=True) #remove rows with blank entries in Customer Segmentation

df["tiprel_1mes"].replace({"": "R"}, inplace=True) 
#In Customer Relation Type, all relations are mentioned except Potential Customers, which were set as blank entries, now changed
df["conyuemp"].replace({"N": "1"}, inplace=True)
#In Spouse Index, all clients that have a spouse are labelled correctly, as per data type description

df['fecha_alta'] = pd.to_datetime(df.fecha_alta)
df['fecha_alta'] = df['fecha_alta'].dt.strftime('%d-%m-%Y') #All date entries are formatted using the same date format

df.drop(df[df["antiguedad"] < 1].index, inplace=True) #All entries that list negative customer seniority are removed

df.drop(df[df["age"] < 18].index, inplace=True)
df.drop(df[df["age"] > 116].index, inplace=True)
#All clients listed as having ages lower than 18 or higher than 116 are eliminated
