import pandas as pd
import pickle

# Read the CSV file into a DataFrame
df = pd.read_csv('linkedArchitects2/mapArchitects2.csv', index_col=0)

# Drop specified columns
columns_to_drop = ['建築家', '日本の都市計画家一覧']
df = df.drop(columns_to_drop, axis=1).drop(columns_to_drop, axis=0, errors='ignore')


dictArchitects = {}

# Iterate through DataFrame indices and columns to create the dictionary
for i in df.index:
    dictLink = {}
    for j in df.columns:
        if df.loc[i][j] != 0:
            dictLink[j] = df.loc[i][j]
    if dictLink:
        dictArchitects[i] = dictLink

with open('dictArchitects.pkl', 'wb') as f:
	pickle.dump(dictArchitects, f)