from utils import Utils
from utils import ListNode
import re
from graphviz import Digraph


DATA_PATH = 'D:\GitHome\SSE\projects\DrawTOP\data'

file_list = Utils.getAllFileInPath(DATA_PATH)
cmd_dict = {}       # id -> ListNode
active_node_dict = {}
id_dict = {}        # system:cmd -> id
cnt = 0
dot = Digraph(name='TOP_graph', format='png')

for file_path in file_list:
    file = open(file_path, 'r', encoding='UTF-8')
    for line in file:
        if re.match("CMD", line):
            cnt += 1
            words = line.split('|')
            key = words[1] + ':' + words[4]
            time = words[3]
            if time != '-':
                active_node_dict[cnt] = True
            else :
                active_node_dict[cnt] = False
            cmd_dict[cnt] = ListNode(id=cnt, cmd=key, time=time, prev=[])
            id_dict[key] = cnt
    file.close()

for file_path in file_list:
    file = open(file_path, 'r', encoding='UTF-8')
    for line in file:
        if re.match("DEPEND", line):
            # #mode|serverid|cmd|depend serverid|depend cmd|depend mode
            words = line.split('|')
            cmd = words[1] + ':' + words[2]
            cmd_id = id_dict[cmd]
            depend = words[3] + ':' + words[4]
            depend_id = id_dict[depend]
            cmd_dict[cmd_id].prev.append(depend_id)
            active_node_dict[depend_id] = True
    file.close()


# draw active nodes
for cmd_id in cmd_dict.keys():
    cmd = cmd_dict[cmd_id].cmd
    depend_id_list = cmd_dict[cmd_id].prev
    time = cmd_dict[cmd_id].time
    if active_node_dict[cmd_id]:
        if time != '-':
            dot.node(str(cmd_id), time + '\n' + cmd, shape='box')
        else:
            dot.node(str(cmd_id), 'MANUAL' + '\n' + cmd, shape='invhouse', color='red')
    
# draw edges
for cmd_id in cmd_dict.keys():
    depend_id_list = cmd_dict[cmd_id].prev
    if len(depend_id_list):
        for depend_id in depend_id_list:
            dot.edge(str(depend_id), str(cmd_id))
            
dot.view()
