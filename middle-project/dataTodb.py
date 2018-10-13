#!/usr/bin/python3
from pymongo import MongoClient
from stat_NBA_data import spider
from datalist import sdict
class InputSpiderData(object):
    def __init__(self,spider_list):
        self.list=spider_list
        self.conn=MongoClient('localhost',27017)
        self.db=self.conn.stu

    def start(self):
        for current_dict in self.list:
            self.insertdata(current_dict)
        self.conn.close()

    def insertdata(self,current_dict):
        for key_value in current_dict.items():
            print(key_value[0])
        self.db[key_value[0]].remove({})
        self.db[key_value[0]].insert(key_value[1])

if __name__=='__main__':
    spider_list=spider()
    # spider_list=sdict()
    obj=InputSpiderData(spider_list)
    obj.start()

