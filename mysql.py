#!/usr/bin/python3

import pymysql

# 打开数据库连接
db = pymysql.connect(host='47.117.67.126',
                     user='debugger',
                     password='Ab12345!',
                     database='SJTUCAT')

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 查询语句
def getById(id):
    # sql = "select * from schoolcat where cat_id = %s" % (id)
    sql = "select * from cathp where id = %s" % (id)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            id = row[0]
            catname = row[1]
            catsex = row[2]
            catcolor = row[3]
            cathabit = row[4]
            catpicture = row[5]

    except:
        print("Error: unable to fetch data")
    # 关闭数据库连接
    # db.close()
    return id, catname, catsex, catcolor, cathabit, catpicture


def getByUrl(url):
    # sql = "select * from schoolcat where cat_id = %s" % (id)
    sql = "select * from cat where picture = '%s';" % (url)
    print(sql)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            id = row[0]
            name = row[1]
            color = row[2]
            description = row[3]
            url = row[4]

            # 打印结果
            print("id=%s,color=%s,des=%s" % \
                  (id, name, color, url, description))
    except:
        print("Error: unable to fetch data")
    # 关闭数据库连接
    # db.close()
    return id, name, color, url, description


def refreshForum():
    sql = "select * from forum order by id desc limit 3;"
    print(sql)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()

    except:
        print("Error: unable to fetch data")
    # 关闭数据库连接
    # db.close()
    return results


def loadForumInfo(inputid):
    sql = "select * from forum where id < %s order by id desc limit 3;" % (inputid)
    print(sql)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
    except:
        print("Error: unable to fetch data")
    # 关闭数据库连接
    # db.close()
    return results


def insertInForum(usrid, title, content, avatar, img, time, likes=0):
    # sql = "select * from schoolcat where cat_id = %s" % (id)
    sql = "insert into forum values (0,'%s','%s','%s','%s','%s','%s',%s)" % (usrid, title, content, avatar, img, time, likes)
    print(sql)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()

    # 关闭数据库连接
    # db.close()
    return


def insert(cat_color, cat_description):
    sql = "insert into schoolcat (color, description) values ('%s','%s')" % (cat_color, cat_description)
    print(sql)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()

    # 关闭数据库连接
    # db.close()
    return
