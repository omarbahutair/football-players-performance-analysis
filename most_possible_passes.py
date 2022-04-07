import networkx as nx

def mostPossiblePasses(graph, property):
    most_possible_passes = []
    for edge in graph.edges(data=True):
        if edge[2]["weight"] >= 5:
            most_possible_passes.append((graph._node[edge[0]][property], graph._node[edge[1]][property]))

    return most_possible_passes
