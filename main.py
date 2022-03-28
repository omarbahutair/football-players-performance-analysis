import openpyxl as xl
import networkx as nx
from matplotlib import pyplot as plt

match_1 = xl.load_workbook("Book1.xlsx")
sheet = match_1["Sheet1"]
names_column = 3
positions_column = 2
players_numbers_column = 1



def generateGraph(position_x, position_y, number_of_players):
    #the position x and y are the rpw and column of the name in the xl_sheet
    graph = nx.DiGraph()
    for number in range(1, number_of_players+1):
        graph.add_node(number)

    for row in range(position_x + 1, position_x + 1 + number_of_players):
        graph._node[row-position_x]['name'] = sheet.cell(row, names_column).value
        graph._node[row-position_x]['position'] = sheet.cell(row, positions_column).value
        graph._node[row-position_x]['number'] = sheet.cell(row, players_numbers_column).value

    for row in range(1, number_of_players+1):
        for column in range(1, number_of_players+1):
            if sheet.cell(row+position_x, column+position_y).value > 0 :
                graph.add_edge(row, column, weight = sheet.cell(row+position_x, column+position_y).value)
    return graph

graph = nx.DiGraph()

graph_0_10 = generateGraph(5, 3, 11)
graph_10_20 = generateGraph(20, 3, 11)
graph_20_30 = generateGraph(35, 3, 11)
graph_30_40 = generateGraph(50, 3, 11)
graph_40_50 = generateGraph(65, 3, 11)
graph_50_60 = generateGraph(80, 3, 11)
graph_60_70 = generateGraph(95, 3, 11)
graph_70_80 = generateGraph(110, 3, 11)
graph_80_90 = generateGraph(125, 3, 12)


