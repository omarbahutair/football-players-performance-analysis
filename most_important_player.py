import networkx as nx

def most_important_player(graph):
    betweenness_and_centrality = nx.centrality.betweenness_centrality(graph)

    keys = []
    values = []
    for k, v in betweenness_and_centrality.items():
        keys.append(k)
        values.append(v)

    max_betweenness_player = graph._node[keys[values.index(max(values))]]['name']
    return max_betweenness_player