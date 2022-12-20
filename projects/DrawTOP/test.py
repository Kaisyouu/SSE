from graphviz import Digraph

dot = Digraph(name='test', format='png', comment='something')
dot.node("1", "09:00:00\nSYSTEM1:START_CMD1", shape='box')
dot.node("2", "10:00:00\nSYSTEM1:START_CMD2", shape='box')
dot.node("3", "10:01:00\nSYSTEM2:START_CMD1", shape='box')
dot.node("4", "10:02:00\nSYSTEM1:START_CMD3", shape='box')
dot.edge('1', '2')
dot.edge('1', '3')
dot.edge('2', '4')
dot.edge('1', '4')


dot.view()
