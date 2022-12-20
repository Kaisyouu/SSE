from graphviz import Digraph

dot = Digraph('Test')
dot.node("1", "Life's too short")
dot.node("2", "I learn Python")
dot.edge('1', '2')

dot.view()
