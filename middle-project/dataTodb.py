#!/usr/bin/python3
from pymongo import MongoClient
from stat_NBA_data import spider
from datalist import sdict
class InputSpiderData(object):
    def __init__(self,spider_dict):
        self.dict=spider_dict
        self.conn=MongoClient('localhost',27017)
        self.db=self.conn.stu

    def start(self):
        for current_class in self.dict.keys():
            self.insertdata(current_class)
        self.conn.close()

    def insertdata(self,current_class):
        self.db.current_class[current_class].remove({})
        for x in self.dict[current_class]:
            self.db.current_class[current_class].insert(x)

if __name__=='__main__':
    spider_dict=spider()
    # spider_dict=sdict()
    obj=InputSpiderData(spider_dict)
    obj.start()

