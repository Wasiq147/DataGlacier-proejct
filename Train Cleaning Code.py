import pandas as pd

df = pd.read_csv(r'/content/drive/MyDrive/Train.csv', header = 0)
df.dropna(subset = ["ind_empleado"], inplace=True) #remove rows with blank entries in Employee Index
df.dropna(subset = ["pais_residencia"], inplace=True) #remove rows with blank entries in Customer's Country Residence
df.dropna(subset = ["sexo"], inplace=True) #remove rows with blank entries in Customer's Sex
df["age"] = df.drop(df[df["age"] == "NA"].index, inplace=True) #remove rows where Customer Age was written as NA

df.drop(df[df["age"] < 18].index, inplace=True)
df.drop(df[df["age"] > 116].index, inplace=True)
#All clients listed as having ages lower than 18 or higher than 116 are eliminated

df.dropna(subset = ["ind_nuevo"], inplace=True) #remove rows with blank entries in Customer Indices

df["antiguedad"] = pd.to_numeric(df["antiguedad"])
df.drop(df[df["antiguedad"] < 0].index, inplace=True) #All entries that list negative Customer Seniority are removed
df.drop(df[df["antiguedad"] == "NA"].index, inplace=True) #remove rows where Customer Seniority was written as NA
df["indrel"] = df.drop(df[df["indrel"] == "NA"].index, inplace=True) #remove rows where Customer Primary status was written as NA

df.dropna(subset = ["tiprel_1mes"], inplace=True) #remove rows with blank entries in Customer Type
df.dropna(subset = ["indresi"], inplace=True) #remove rows with blank entries in Residence Index
df.dropna(subset = ["indext"], inplace=True) #remove rows with blank entries in Foreigner Index
df.dropna(subset = ["canal_entrada"], inplace=True) #remove rows with blank entries in Channls Used by Customers to Join
df.dropna(subset = ["indfall"], inplace=True) #remove rows with blank entries in Deceased Index

df["tipodom"] = df.drop(df[df["tipodom"] == "NA"].index, inplace=True) #remove rows where Customer Address Type was written as NA
df.dropna(subset = ["nomprov"], inplace=True) #remove ros with blank entries in Province Names
df["ind_actividad_cliente"] = df.drop(df[df["ind_actividad_cliente"] == "NA"].index, inplace=True) #remove rows where Customer Activity Index was written as NA
df.dropna(subset = ["segmento"], inplace=True) #remove rows with blank entries in Customer Segmentation

df.dropna(subset = ["fecha_alta"], inplace=True) #remove rows with blank entries for when customers became holders at bank

df['fecha_alta'] = pd.to_datetime(df.fecha_alta)
df['fecha_alta'] = df['fecha_alta'].dt.strftime('%d-%m-%Y') #All date entries are formatted using the same date format
