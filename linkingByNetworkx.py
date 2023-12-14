import networkx as nx
import pandas as pd
from pyvis.network import Network

edges = pd.DataFrame({'source': ["A","A","A","B","B","C","C","D","E"],
                  'target': ["B","C","D","D","C","E","D","E","A"]}) 
G = nx.from_pandas_edgelist(edges, edge_attr=True)

def re_construct_network(edge_df):
    #nodeの生成
    G = nx.DiGraph
    G = nx.from_pandas_edgelist(df2,source="source",target="target") 

    #node_df生成。一回edgelistからnetworkxを経由してノードリストを生成しておく。
    node_df=pd.DataFrame(list(G.nodes()),columns=['nodes']).sort_values(by='nodes')  
     #この段階でnode_dfに列を追加して属性候補を入れても良い。  

    #edgelistの再生成（）
    edges=[]
    for index, row in edge_df.iterrows():
        edges.append((row[0],row[1]))
    
    # #nodeをpyvisに読ませる＋同時にedgeをpyvisに読ませる。
    # g = Network(height='500px', width='750px',directed=True)
    # node_id = node_df['nodes'].tolist()　#
    # node_x = ~~(出力時のx位置) #lambda式などでの処理もOK
    # node_y = ~~（出力時のy位置)
    # node_value = node_df['///'].tolist()
    # node_title = node_df['~~~'].tolist()
    # node_color = node_df['$$$'].apply(setcolor).tolist()　#色指定の関数を外に出してlamda式で使う。
    # node_label = node_df["%%%"].astype(str).tolist()
        
    #add_nodesで指定できるのが ["size", "value", "title", "x", "y", "label", "color"]
    g.add_nodes()
    g.add_edges(edges)
    g.toggle_physics(True) #動かしたい場合
    g.show_buttons(True)   #出力後の調整バーを入れる場合
    g.show("network_pyvis.html")

re_construct_network(edges)