#!/usr/bin/env python
# coding: utf-8

# In[1]:


from partial_index import partial_index

class Index:
    index = {}
    
#     read the index
    def read_partial_index(self, doc_id: int, p_index: partial_index):
        for i in p_index.index:
            if i not in self.index:
                self.index[i] = {}
            self.index[i][doc_id] = p_index.index[i]
            
# write down the finally file
    def write_file(self, filename: str):
        file = open(filename + ".idx", "w")
        file_dic = open(filename + ".dict", "w")
        for i, j in ((i, self.index[i]) for i in sorted(self.index)):
            count = 0
            file_dic.write(i + ", " + str(len(j)) + "\n")
            for doc in j:
                count += len(j[doc])
            file.write(i + ", " + str(count) + ":<")
            for doc in j:
                file.write(str(doc) + ", " + str(len(j[doc])) + ":<")
                fr = True
                for pos in j[doc]:
                    if fr:
                        file.write(str(pos))
                        fr = False
                    else:
                        file.write(", " + str(pos))
                file.write(">;")
            file.write(">;\n")
        file.close()
        file_dic.close()


# In[ ]:




