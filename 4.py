import pymysql

# 连接数据库
db = pymysql.connect(host="localhost",
                     port=3306,
                     user="root",
                     password="123456",
                     database="text",
                     charset="utf8")
# 生成游标对象
cur = db.cursor()
# with open("/home/tarena/1908/month02/day02/timg.jpeg","rb") as f:
#     data=f.read()
# try:
#     sql="insert into image values (1,%s,%s);"
#     cur.execute(sql, ['ycy.jpg',data])
#     db.commit()
# except Exception as e:
#     db.rollback()
#     print(e)

sql = "select filename,img from image where filename='ycy.jpg';"
cur.execute(sql)
data = cur.fetchone()
with open(data[0],"wb") as f:
    f.write(data[1])
cur.close()
db.close()
