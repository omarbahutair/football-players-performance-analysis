import networkx as nx

def mostPossiblePasses(graph):
    most_possible_passes = []
    for edge in graph.edges(data=True):
        if edge[2]["weight"] >= 5:
            most_possible_passes.append(edge)

    return most_possible_passes
