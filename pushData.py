from py2neo import Graph, Node, Relationship, NodeMatcher,Subgraph
from py2neo.matching import RelationshipMatcher
import pandas as pd
# 连接数据库
graph = Graph("http://localhost:7500", username="", password='')
graph.run('match (n) detach delete n')


df = pd.read_excel("r2.xlsx")

created_nodes_str_list1 = []
created_nodes_str_list2 = []
created_nodes = []

for index in range(df[:].shape[0]) :
    node1_name,node1_type,edge,edge_type,node2_name,node2_type = df.iloc[index,1],df.iloc[index,2],df.iloc[index,3],df.iloc[index,4],df.iloc[index,5],"law"
    #	head_entity	head_entity_type	relation	relation_type	tail_entity	tail_entity_type
    
    if node1_name+node1_type not in created_nodes_str_list1:
        created_nodes_str_list1.append(node1_name+node1_type) 

        a = Node(node1_type, name=node1_name)
        created_nodes.append(a)

    if node2_name not in created_nodes_str_list2:
        created_nodes_str_list2.append(node2_name) 

        b = Node("law", name=node2_name)
        created_nodes.append(b)


nodes=Subgraph(created_nodes)
graph.create(nodes)

created_relations = []
for index in range(df[:].shape[0]) :
    node1_name,node1_type,edge,edge_type,node2_name,node2_type = df.iloc[index,1],df.iloc[index,2],df.iloc[index,3],df.iloc[index,4],df.iloc[index,5],"law"
    #	head_entity	head_entity_type	relation	relation_type	tail_entity	tail_entity_type
    a=graph.nodes.match(node1_type, name=node1_name).first()
    b=graph.nodes.match(node2_type, name=node2_name).first()

    rel_d=Relationship(a,edge,b)
    created_relations.append(rel_d)

A=Subgraph(relationships=created_relations)

graph.create(A)
