import pymysql
class DataBase:
    def __init__(self):
        self.db = pymysql.connect(host="localhost",
                     port=3306,
                     user="root",
                     password="123456",
                     database="users",
                     charset="utf8")
        self.cur = self.db.cursor()
    def close(self):
        self.cur.close()
        self.db.close()


    def register(self,name,passwd):
        sql = "select id from user where name=%s;"%name
        self.cur.execute(sql)
        result = self.cur.fetchone()
        if result:
            print("该用户名存在!")
            return
        sql = "insert into user values (%s,%s);"
        self.cur.execute(sql,[name,passwd])
        self.db.commit()
    def enter(self,name,passwd):
        sql = "select passwd from user where name=%s;" % name
        password=self.cur.execute(sql)
        if password:
            print("该用户名存在!")
            return
        elif password==passwd:
            print("登录成功!")
        else:
            print("密码错误!")

