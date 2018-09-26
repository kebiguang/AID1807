#将文件以GRID方案存放到数据库
from pymongo import MongoClient
import gridfs

conn=MongoClient('127.0.0.1',27017)
db=conn.grid

fs=gridfs.GridFS(db)
f=open('hhh.jpg','rb')

fs.put(f.read(),filename='kkk.jpg')

conn.close()