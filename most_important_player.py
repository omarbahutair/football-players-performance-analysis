import networkx as nx


def get_key(my_dict, val):
    for key, value in my_dict.items():
         if val == value:
             return key


def sortKeysByValue(dictionary):
    dict_vals = list(dictionary.values())
    dict_keys = list(dictionary.keys())
    dict_vals.sort()
    sorted_dict_keys = []
    for val in dict_vals:
        for key in dict_keys:
            if dictionary[key] == val:
                sorted_dict_keys.append(key)
                del dictionary[key]
                dict_keys.remove(key)
                break

    return sorted_dict_keys


def mostImportantPlayer(graph):
    betweenness_and_centrality = nx.centrality.betweenness_centrality(graph)
    print(betweenness_and_centrality)
    betweenness_and_centrality_2 = sorted(betweenness_and_centrality)
    print(betweenness_and_centrality_2)
    keys = []
    values = []
    for k, v in betweenness_and_centrality.items():
        keys.append(k)
        values.append(v)
    #max_betweenness_player = graph._node[keys[values.index(max(values))]]['name']
    #return max_betweenness_player




simple_graph = nx.DiGraph()
simple_graph.add_nodes_from([1, 2, 3, 4, 5])
simple_graph.add_edge(1, 2)
simple_graph.add_edge(2, 4)
simple_graph.add_edge(5, 3)
simple_graph.add_edge(4, 1)
simple_graph.add_edge(2, 3)
betweenness = nx.centrality.betweenness_centrality(simple_graph)
betweenness_sorted_keys = sortKeysByValue(betweenness)
print(betweenness)
print(betweenness_sorted_keys)
print(betweenness)
mostImportantPlayer(simple_graph)