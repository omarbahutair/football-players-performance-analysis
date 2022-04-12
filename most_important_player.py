import networkx as nx


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


def playersImportance(graph, property):
    betweenness = nx.betweenness_centrality(graph)
    sortedKeys = sortKeysByValue(nx.betweenness_centrality(graph))
    sortedKeys.reverse()
    sortedProperty = {}
    for key in sortedKeys:
        sortedProperty[graph._node[key][property]] = betweenness[key]

    return sortedProperty