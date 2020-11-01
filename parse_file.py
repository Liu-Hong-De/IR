#!/usr/bin/env python
# coding: utf-8

# In[9]:


import os

from WARC_information import WARC_information

class parse_file:
    encoding = 'ISO-8859-1'
    position = 0
    
    def __init__(self, file):
        self.file = file
        self.file_size = os.stat(self.file).st_size
        self.f = open(self.file, "rb")
        
    def read_file(self):
        while True:
            self.position = self.f.tell()    # current file position
            if self.f.tell() == self.file_size:    # if read end
                return None
            line = self.f.readline().decode(self.encoding)
            if line[0] == 'W':
                break
            
        information = WARC_information()    # get the WARCindormation
        information.pos = self.position
        information.version = line[:-1]
            
        while True:
            line = self.f.readline().decode(self.encoding)[:-1].split(": ", 1)    # read each line and split by ': '
                
            if line[0] == 'Content-Length':
                information.length = int(line[1].strip())
                information.content = self.f.read(information.length).decode(self.encoding)
                break
            else:
                information.header[line[0].strip()] = line[1].strip()
        return information


# In[ ]:




