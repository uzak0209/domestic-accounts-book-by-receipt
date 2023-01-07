import mysql.connector
import identify_chara
import pandas as pd
cnx = None

try:
    cnx = mysql.connector.connect(
        user='',  # ユーザー名
        password=',  # パスワード
        db='mysql',
        host=''  # ホスト名(IPアドレス）
    )

    if cnx.is_connected:
        print("Connected!")
    cursor = cnx.cursor(buffered=True)

    sql = ('''
    INSERT INTO receipt 
        (merchadise,value)
    VALUES 
        (%s, %s)
    
    ''')
    data=identify_chara.identify()
    cursor.executemany(sql,data)
    cnx.commit()
    print(f"{cursor.rowcount}records inserted.")
    sql=('''SELECT * FROM receipt;''')
    cursor.execute(sql)
    data=cursor.fetchall()
    cursor.close()
    print(pd.DataFrame(data,columns=["id","商品名","値段","日時"]))
except Exception as e:
    print(f"Error Occurred: {e}")
finally:
    if cnx is not None and cnx.is_connected():
        cnx.close()
