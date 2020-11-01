#!/usr/bin/env python
# coding: utf-8

# In[2]:


class partial_index:
    index = {}
    
    def __init__(self):
        self.index = dict()    # build dictionary
        
    def dump(self, filename):
        file = open(filename, "w")
        for i in self.index:
            content = i + " "
            for j in self.index[i]:
                content += str(j) + ","
            content = content[:-1] + "\n"
            file.write(content)
        file.close()
    
    def push(self, word, pos):
        if word in self.index:
            self.index[word].append(pos)
        else:
            self.index[word] = [pos]
    
    @staticmethod
    def read(filename):
        file = open(filename, 'r')
        all_line = file.readlines()
        index = partial_index()
        for line in all_line:
            content = line
            content = content.split(" ")
            val = content[1].split(',')
            for j in val:
                index.push(content[0], int(j))
        file.close()
        return index

