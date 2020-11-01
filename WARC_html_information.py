#!/usr/bin/env python
# coding: utf-8

# In[3]:


import re
import nltk

from html.parser import HTMLParser
from partial_index import partial_index
from stem import stem
from nltk.corpus import stopwords

class WARC_html_information(HTMLParser):
    line_count = []
    offset = 0
    index = partial_index()
    position = 0
    case_folding = False
    stopword_remove = False
    stemming = False
    nltk.download('stopwords')
    stopwords = stopwords.words('english')
    
    def __init__(self):
        HTMLParser.__init__(self)
        self.index = partial_index()
        self.line_count = []
        
        
    def cal_offset(self, line_num, offset):
        return self.line_count[line_num-1] + offset
    
    def feed(self, data):
        all_line = data.split('\n')
        count = 1
        self.line_count.append(0)
        
        for line in all_line:
            self.line_count.append(self.line_count[count-1] + len(line) + 1)
            count += 1
        HTMLParser.feed(self, data)
    
    def handle_data(self, data):
        if self.lasttag not in ['script', 'style']:
            offset = self.cal_offset(self.getpos()[0], self.getpos()[1]) + self.offset
            word = re.compile('[A-Za-z]+')
            words = word.finditer(data)    # find all iteration
            for w in words:
                if WARC_html_information.stopword_remove:
                    if w.group(0).lower() in self.stopwords:
                        continue
                if WARC_html_information.case_folding:
                    if WARC_html_information.stemming:
                        self.index.push(stem(w.group(0).lower()), self.position)
                    else:
                        self.index.push(w.group(0).lower(), self.position)
                else:
                    if WARC_html_information.stemming:
                        self.index.push(stem(w.group(0)), self.position)
                        self.index.push(stem(w.group(0)), w.start() + offset)
                    else:
                        self.index.push(w.group(0), self.position)
                self.position += 1    # calculate the word position


# In[ ]:




