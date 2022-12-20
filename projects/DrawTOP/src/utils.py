import os

class ListNode():
    def __init__(self, id=0, cmd="", time="", prev=None):
        self.id = id
        self.cmd = cmd
        self.time = time
        self.prev = prev

class Utils():
    def getAllFileInPath(path):
        '''
        input: 文件路径path
        '''
        file_list = []
        files = os.listdir(path)
        for file in files:
            file_list.append(os.path.join(path,file))
        return file_list