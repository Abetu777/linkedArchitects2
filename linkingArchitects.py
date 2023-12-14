from pyvis.network import Network
import pandas as pd

df = pd.read_csv('mapArchitects.csv', index_col=0)
df = df.drop('建築家')
df = df.drop('建築家', axis=1)
df = df.drop('日本の都市計画家一覧')
df = df.drop('日本の都市計画家一覧', axis=1)


net = Network(notebook=True)

# for i in df.columns:
#     net.add_node(i)

# Add edges
for i in list(df.index):
    for j in list(df.columns):
        if df.loc[i][j] == 0:
            pass
        elif i == j:
            pass
        else:
            net.add_node(i)
            net.add_node(j)
            net.add_edge(i, j, width=int(df.loc[i][j]))
            
net.show_buttons(filter_=['physics'])
net.show('linkedArchitects.html')



