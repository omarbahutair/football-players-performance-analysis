import openpyxl as xl
import networkx as nx
import most_important_player
from most_important_player import playersImportance
from most_possible_passes import mostPossiblePasses
from matplotlib import pyplot as plt
import find_good_cliques as fgc

match_1 = xl.load_workbook("Book1.xlsx")
sheet = match_1["Sheet1"]
names_column = 3
positions_column = 2
players_numbers_column = 1
total_graph = nx.DiGraph()


def generateGraph(position_x, position_y, number_of_players):
    #the position x and y are the row and column of the name in the xl_sheet
    graph = nx.DiGraph()
    for number in range(1, number_of_players+1):
        graph.add_node(number)

    for row in range(position_x + 1, position_x + 1 + number_of_players):
        graph._node[row-position_x]['name'] = sheet.cell(row, names_column).value
        graph._node[row-position_x]['position'] = sheet.cell(row, positions_column).value
        graph._node[row-position_x]['number'] = sheet.cell(row, players_numbers_column).value

    for row in range(1, number_of_players+1):
        for column in range(1, number_of_players+1):
            if sheet.cell(row+position_x, column+position_y).value > 0:
                graph.add_edge(row, column, weight=sheet.cell(row+position_x, column+position_y).value)
                if (row, column) in total_graph.edges():
                    list(total_graph.edges(data=True))[list(total_graph.edges()).index((row, column))][2]['weight'] +=\
                        sheet.cell(row+position_x, column+position_y).value
                else:
                    total_graph.add_edge(row, column, weight=sheet.cell(row+position_x, column+position_y).value)
    return graph


graph_0_10 = generateGraph(5, 3, 14)
graph_10_20 = generateGraph(23, 3, 14)
graph_20_30 = generateGraph(41, 3, 14)
graph_30_40 = generateGraph(59, 3, 14)
graph_40_50 = generateGraph(77, 3, 14)
graph_50_60 = generateGraph(95, 3, 14)
graph_60_70 = generateGraph(113, 3, 14)
graph_70_80 = generateGraph(131, 3, 14)
graph_80_90 = generateGraph(149, 3, 14)

graphs = [graph_0_10, graph_10_20, graph_30_40, graph_40_50, graph_50_60, graph_60_70, graph_70_80, graph_80_90]


for graph in graphs:
    for node in graph.nodes(data=True):
        if not (node in list(total_graph.nodes(data=True))):
            total_graph.add_node(node[0])
            total_graph._node[node[0]]['name'] = node[1]['name']
            total_graph._node[node[0]]['position'] = node[1]['position']
            total_graph._node[node[0]]['number'] = node[1]['number']




cliques = list(nx.enumerate_all_cliques(total_graph.to_undirected()))


#to find all good cliques
best_cliques = [] # if each node has an out degree higher than 10 then its a good clique

for clq in cliques:
    if fgc.isGoodClique(clq, total_graph, 10) and len(list(clq)) <= 3:
        best_cliques.append(clq)


for clq in best_cliques:
    print("clique: " + str(best_cliques.index(clq)))
    fgc.printClq(clq, total_graph, "name")
    print("\n\n")

sorted_players = playersImportance(total_graph,"name")
print(sorted_players)

most_possible_passes = mostPossiblePasses(total_graph, "name")
print(most_possible_passes)