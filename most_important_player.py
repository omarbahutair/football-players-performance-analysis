import networkx as nx

"""
def get_key(my_dict, val):
    for key, value in my_dict.items():
         if val == value:
             return key
"""

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
    sortedKeys = sortKeysByValue(nx.betweenness_centrality(graph))
    sortedProperty = []
    for key in sortedKeys:
        sortedProperty.append(graph._node[key][property])

    return sortedProperty