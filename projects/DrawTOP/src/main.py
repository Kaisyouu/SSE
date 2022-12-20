import re
from utils import ListNode

file = open('../data/drmm_cfg.cfg', 'r')
cmd_dict = {}
for line in file:
    if re.match("CMD", line):
        words = line.split('|')
        key = words[1] + ':' + words[4]
        cmd_dict[key] = ListNode(cmd=key, time=words[3], prev=[])
    if re.match("DEPEND", line):
        words = line.split('|')
        key = words[1] + ':' + words[2]
        if key in cmd_dict.keys():
            cmd_dict[key].prev.append(words[3] + ':' + words[4])

for key, value in cmd_dict.items():
    print('{key}:{value}'.format(key=key, value=value))
print('debug here')