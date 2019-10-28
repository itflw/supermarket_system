import pymysql
import goods


def get_all():
    conn = pymysql.Connect(host="localhost", user="root", passwd="fqw0408!", db="goodsdb")
    cur = conn.cursor()
    cur.execute("select * from goods")
    rows = cur.fetchall()
    conn.close()
    return rows

def get_byid(g):
    conn = pymysql.Connect(host="localhost", user="root", passwd="fqw0408!", db="goodsdb")
    cur = conn.cursor()
    cur.execute("select * from goods where gid = %s", (g.get_gid(), ))
    row = cur.fetchone()
    conn.close()
    return row

def get_byname(g):
    conn = pymysql.Connect(host="localhost", user="root", passwd="fqw0408!", db="goodsdb")
    cur = conn.cursor()
    cur.execute("select * from goods where gname = %s", (g.get_gname(), ))
    row = cur.fetchone()
    conn.close()
    return row

def get_blurname(blur_name):
    # 模糊名称查询
    conn = pymysql.Connect(host="localhost", user="root", passwd="fqw0408!", db="goodsdb")
    cur = conn.cursor()
    sql = "select * from goods where gname like '%%{}%%'".format(blur_name)
    cur.execute(sql)
    row = cur.fetchall()
    conn.close()
    return row

def add_good(g):
    conn = pymysql.Connect(host="localhost", user="root", passwd="fqw0408!", db="goodsdb")
    cur = conn.cursor()
    try:
        cur.execute("insert into goods values(null, %s, %s, %s)", (g.get_gname(), g.get_gprice(), g.get_gnum(), ))
        conn.commit()
    except:
        conn.rollback()
    finally:
        conn.close()

def update_good(g):
    conn = pymysql.Connect(host="localhost", user="root", passwd="fqw0408!", db="goodsdb")
    cur = conn.cursor()
    try:
        cur.execute("update goods set gname = %s, gprice = %s, gnum = %s where gid = %s", (g.get_gname(), g.get_gprice(), g.get_gnum(), g.get_gid(), ))
        conn.commit()
    except:
        conn.rollback()
    finally:
        conn.close()

def delete_good(g):
    '''
    通过ID删除
    '''
    conn = pymysql.Connect(host="localhost", user="root", passwd="fqw0408!", db="goodsdb")
    cur = conn.cursor()
    try:
        cur.execute("delete from goods where gid = %s", (g.get_gid(), ))
        conn.commit()
    except:
        conn.rollback()
    finally:
        conn.close()

def delete_good_byname(g):
    '''
    通过名称删除
    '''
    conn = pymysql.Connect(host="localhost", user="root", passwd="fqw0408!", db="goodsdb")
    cur = conn.cursor()
    try:
        cur.execute("delete from goods where gname = %s", (g.get_gname(), ))
        conn.commit()
    except:
        conn.rollback()
    finally:
        conn.close()

#通过id查找
# g = goods.good()
# g.set_gid(1001)
# print(get_byid(g))
# exit(1)

#通过name查找
# g = goods.good()
# g.set_gname("飞旺")
# print(get_byname(g))

# 添加商品
# g = goods.good()
# g.set_gname("百事可乐")
# g.set_gprice(3.00)
# g.set_gnum(95)
# print(add_good(g))
# print(get_all())

# 更新商品
# g = goods.good()
# g.set_gid(1000)
# g.set_gname("茉莉花茶")
# g.set_gprice(3.00)
# g.set_gnum(80)
# update_good(g)
# print(get_all())

#删除商品
# g = goods.good()
# g.set_gid(1004)
# delete_good(g)
# print(get_all())