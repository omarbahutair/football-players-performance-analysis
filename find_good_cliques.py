import networkx as nx


def getOutDegreeOfANode(node, graph):
    out_degree = 0
    for edge in graph.edges():
        if node == edge[0]:
            out_degree+=graph.edges[edge]["weight"]

    return out_degree


def printClq(clq, graph, property):
    for nde in clq:
        print(graph._node[nde][property])


def isGoodClique(clq, graph, minimal_out_degree):
    sub_graph = graph.subgraph(clq)
    sum_out_degree = 0
    for nde in clq:
        if getOutDegreeOfANode(nde, sub_graph) < minimal_out_degree:
            return False;

    return True;